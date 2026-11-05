import {initializeApp} from "firebase-admin/app";
import {onRequest} from "firebase-functions/v2/https";
import {setGlobalOptions} from "firebase-functions/v2";
import {defineSecret} from "firebase-functions/params";

initializeApp();
setGlobalOptions({region: "asia-south1", maxInstances: 3});

const PMC_API_KEY = defineSecret("PMC_API_KEY");

const allowedOrigins = new Set([
  "https://itrunks.github.io",
  "http://localhost:8081",
  "http://localhost:19006"
]);

const providerBaseUrl = "https://letspickmycar.com/api/v1";

export const apiHealth = onRequest(
  {cors: [...allowedOrigins], secrets: [PMC_API_KEY]},
  (_request, response) => {
    response.set("Cache-Control", "no-store");
    response.status(200).json({
      service: "motivo-api",
      status: "ok",
      region: "asia-south1",
      providers: {
        primary: PMC_API_KEY.value() ? "configured" : "not_configured",
        fallback: "not_configured"
      }
    });
  }
);

// This endpoint checks the provider account balance. It does not request car
// catalogue data, so it is suitable for validating credentials before using
// metered catalogue endpoints.
export const providerBalance = onRequest(
  {cors: [...allowedOrigins], secrets: [PMC_API_KEY]},
  async (request, response) => {
    response.set("Cache-Control", "no-store");

    if (request.method !== "GET") {
      response.set("Allow", "GET");
      response.status(405).json({error: "method_not_allowed"});
      return;
    }

    const apiKey = PMC_API_KEY.value();
    if (!apiKey) {
      response.status(503).json({error: "provider_not_configured"});
      return;
    }

    try {
      const upstream = await fetch(`${providerBaseUrl}/balance`, {
        method: "GET",
        headers: {
          Authorization: `Bearer ${apiKey}`,
          Accept: "application/json"
        },
        signal: AbortSignal.timeout(10000)
      });

      if (!upstream.ok) {
        // Do not forward provider error bodies or credentials to the client.
        response.status(502).json({
          error: "provider_request_failed",
          providerStatus: upstream.status
        });
        return;
      }

      const data: unknown = await upstream.json();
      response.status(200).json({
        provider: "lets-pick-my-car",
        status: "connected",
        data
      });
    } catch {
      response.status(502).json({error: "provider_unavailable"});
    }
  }
);

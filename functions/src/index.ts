import {initializeApp} from "firebase-admin/app";
import {getFirestore} from "firebase-admin/firestore";
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


// Public, read-only pilot endpoint. Only records with status="published" are
// eligible. Draft/review/rejected records are never returned.
export const catalogueVariants = onRequest(
  {cors: [...allowedOrigins]},
  async (request, response) => {
    response.set("Cache-Control", "public, max-age=300, stale-while-revalidate=600");
    response.set("Vary", "Origin");

    if (request.method !== "GET") {
      response.set("Allow", "GET");
      response.status(405).json({error: "method_not_allowed"});
      return;
    }

    const readParam = (key: string): string | undefined => {
      const value = request.query[key];
      return typeof value === "string" ? value.trim() : undefined;
    };

    const modelId = readParam("modelId");
    const fuel = readParam("fuel");
    const transmission = readParam("transmission");
    const pageToken = readParam("pageToken");
    const rawLimit = readParam("limit") ?? "20";
    const limit = Number(rawLimit);

    if ((request.query.modelId !== undefined && !modelId) ||
        (request.query.fuel !== undefined && !fuel) ||
        (request.query.transmission !== undefined && !transmission) ||
        (request.query.pageToken !== undefined && !pageToken)) {
      response.status(400).json({error: "invalid_query_parameter"});
      return;
    }
    if (modelId && modelId.length > 100) {
      response.status(400).json({error: "invalid_model_id"});
      return;
    }
    const fuels = new Set([
      "petrol", "diesel", "cng", "lpg", "mild_hybrid",
      "strong_hybrid", "plug_in_hybrid", "electric"
    ]);
    const transmissions = new Set([
      "manual", "amt", "cvt", "dct", "torque_converter", "single_speed", "other"
    ]);
    if (fuel && !fuels.has(fuel)) {
      response.status(400).json({error: "invalid_fuel"});
      return;
    }
    if (transmission && !transmissions.has(transmission)) {
      response.status(400).json({error: "invalid_transmission"});
      return;
    }
    if (!Number.isInteger(limit) || limit < 1 || limit > 50) {
      response.status(400).json({error: "limit_must_be_between_1_and_50"});
      return;
    }
    if (pageToken && (pageToken.length > 150 || pageToken.includes("/"))) {
      response.status(400).json({error: "invalid_page_token"});
      return;
    }

    try {
      const db = getFirestore();
      const variants = db.collection("variants");
      let query = variants.where("status", "==", "published").orderBy("__name__").limit(200);

      if (pageToken) {
        const cursor = await variants.doc(pageToken).get();
        if (!cursor.exists) {
          response.status(400).json({error: "invalid_page_token"});
          return;
        }
        query = query.startAfter(cursor);
      }

      const snapshot = await query.get();
      const items = snapshot.docs
        .map((doc) => ({id: doc.id, ...doc.data()}))
        .filter((item) =>
          (!modelId || item.modelId === modelId) &&
          (!fuel || item.fuel === fuel) &&
          (!transmission || item.transmission === transmission)
        )
        .slice(0, limit);

      const hasMore = snapshot.size === 200;
      response.status(200).json({
        schemaVersion: 1,
        items,
        pageToken: hasMore ? snapshot.docs[snapshot.docs.length - 1].id : null
      });
    } catch {
      response.status(500).json({error: "catalogue_unavailable"});
    }
  }
);

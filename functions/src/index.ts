import {initializeApp} from "firebase-admin/app";
import {onRequest} from "firebase-functions/v2/https";
import {setGlobalOptions} from "firebase-functions/v2";

initializeApp();
setGlobalOptions({region: "asia-south1", maxInstances: 3});

const allowedOrigins = new Set([
  "https://itrunks.github.io",
  "http://localhost:8081",
  "http://localhost:19006"
]);

export const apiHealth = onRequest({cors: [...allowedOrigins]}, (_request, response) => {
  response.status(200).json({
    service: "motivo-api",
    status: "ok",
    region: "asia-south1",
    providers: {
      primary: "not_configured",
      fallback: "not_configured"
    }
  });
});

// Provider endpoints are intentionally not guessed. Add them only after
// confirming the provider's official API contract, authentication and licence.

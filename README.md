# Motivo

React Native + Expo + TypeScript car research and comparison website, built for web first and designed to expand to iOS and Android.

## Run locally

```bash
npm install
npx expo start --web
```

## Stack

- Expo SDK 54
- React Native Web
- TypeScript strict mode
- Expo Router
- Firebase / Cloud Firestore
- Firebase Cloud Functions (Node.js 22)

## Current state

The responsive shortlist UI supports budget, fuel, transmission, body style and multi-priority filters. The production vehicle array is intentionally empty: no fabricated vehicle records are shown. Until the verified catalogue is connected, the app will show an empty state rather than invented cars, prices or specifications.

## Firebase and security

The Firebase project is `motivo-car-research`. Client initialization is in `src/lib/firebase.ts`. Firestore rules currently deny all client reads and writes. Keep client writes denied; public catalogue access should be mediated through validated, read-only HTTPS endpoints. Trusted ingestion must use Firebase Admin SDK in a protected environment.

Firebase web configuration is public client configuration, not a server secret. Restrict the API key to the required Firebase APIs and production website domain in Google Cloud. Never add service-account credentials or provider API secrets to the frontend or Git.

Cloud Functions are configured in `firebase.json` for Node.js 22. The current functions are health and provider-balance checks only; production catalogue endpoints are not implemented yet. The presence of deployment configuration does not prove that functions or Firestore rules have been deployed.

The optional Let's Pick My Car provider integration is not the Motivo catalogue source of truth. Do not call metered catalogue endpoints or spend provider credits without explicit approval and a review of licence, field coverage and cost.

## Vehicle data policy

Every published vehicle fact must retain exact brand/model/variant, model year or generation applicability, source references, last-verified date and a clear status. Separate official, estimated and user-reported prices/mileage. Unknown values remain unknown. Public availability does not automatically grant redistribution or commercial-use rights.

Research reports under `research/` are audit material; they are not automatically production catalogue records.

## Beta launch

See [BETA_LAUNCH_CHECKLIST.md](./BETA_LAUNCH_CHECKLIST.md) for the current readiness audit, phased checklist, blockers and release gates.

## Deployment

GitHub Pages deployment is automated through `.github/workflows/deploy-pages.yml`. TypeScript checks run through `.github/workflows/typecheck.yml`.

Live web preview: https://itrunks.github.io/motivo

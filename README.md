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
- React Native Reanimated and Gesture Handler
- Expo Linear Gradient and Vector Icons

## Current state
Responsive car shortlist UI with budget, fuel, transmission, body style and priorities filters. Fictional demo vehicles have been removed.

## Firebase
The web app is registered with Firebase project `motivo-car-research`. Firebase client initialization is in `src/lib/firebase.ts`; it exports the app and Firestore client. Firestore is configured in production mode, so client reads/writes remain denied until explicit security rules are deployed.

Firebase web configuration is public client configuration. Restrict the API key to the required Firebase APIs and the production website domain in Google Cloud. Never add service-account credentials or provider API secrets to the frontend.

The current GitHub Pages deployment is static. Firebase Spark does not provide Cloud Functions; a secure server-side proxy for third-party vehicle APIs will need an eligible backend runtime. Do not expose a provider API key in browser code.

Responsive car shortlist UI with budget, fuel, transmission, body style and priorities filters. Demo vehicle data is deliberately fictional and must not be used for purchase decisions. Verified production data needs exact variant/year, city, source date and confidence metadata.

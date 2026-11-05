import {getApp,getApps,initializeApp} from 'firebase/app';
import {getFirestore} from 'firebase/firestore';

// Firebase web configuration is public client configuration, not a server secret.
// Restrict this API key to the required APIs and Motivo web domains in Google Cloud.
const firebaseConfig={
 apiKey:"AIzaSyAD671HM6jy7ZQBF3uoNENjnduOSVhUrXE",
 authDomain:"motivo-car-research.firebaseapp.com",
 projectId:"motivo-car-research",
 storageBucket:"motivo-car-research.firebasestorage.app",
 messagingSenderId:"530874011057",
 appId:"1:530874011057:web:bca0816ee1d9805d36c190",
 measurementId:"G-ZSZ0Q4XYW1"
};

export const firebaseApp=getApps().length?getApp():initializeApp(firebaseConfig);
export const firestore=getFirestore(firebaseApp);

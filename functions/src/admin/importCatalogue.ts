import {readFile} from "node:fs/promises";
import {initializeApp, getApps} from "firebase-admin/app";
import {getFirestore} from "firebase-admin/firestore";

type ApprovedRecord = {
  id: string;
  entityType: "variant" | "price";
  publicationStatus: "draft";
  source: {sourceId: string; url: string; retrievedAt: string};
  sourceApproval: {
    reviewStatus: "approved";
    commercialReuseAllowed: "yes";
    redistributionAllowed: "yes";
    sourceUrl: string;
    termsUrl: string;
    licenseName: string;
  };
  [key: string]: unknown;
};

function parseArgs(argv: string[]) {
  const args = new Set(argv);
  const batchIndex = argv.indexOf("--batch-id");
  const batchId = batchIndex >= 0 ? argv[batchIndex + 1] : "";
  if (!batchId || !/^[a-zA-Z0-9_-]{3,80}$/.test(batchId)) {
    throw new Error("Provide --batch-id with 3-80 safe characters");
  }
  const fileIndex = argv.indexOf("--input");
  const input = fileIndex >= 0 ? argv[fileIndex + 1] : "";
  if (!input) throw new Error("Provide --input with an approved JSONL file");
  return {write: args.has("--write"), batchId, input};
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const raw = await readFile(args.input, "utf8");
  const records: ApprovedRecord[] = raw.split(/\r?\n/).filter(Boolean).map((line, index) => {
    let value: ApprovedRecord;
    try { value = JSON.parse(line) as ApprovedRecord; }
    catch { throw new Error(`Invalid JSON on line ${index + 1}`); }
    if (!/^[a-z0-9-]{1,100}$/.test(value.id)) throw new Error(`Invalid record id on line ${index + 1}`);
    if (value.publicationStatus !== "draft") throw new Error(`Non-draft record on line ${index + 1}`);
    if (!value.source?.sourceId || !value.source?.url || !value.source?.retrievedAt) throw new Error(`Missing provenance on line ${index + 1}`);
    const approval = value.sourceApproval;
    if (approval?.reviewStatus !== "approved" || approval.commercialReuseAllowed !== "yes" || approval.redistributionAllowed !== "yes" || approval.sourceUrl !== value.source.url || !approval.termsUrl || !approval.licenseName) {
      throw new Error(`Missing explicit source reuse approval on line ${index + 1}`);
    }
    if (value.entityType !== "variant" && value.entityType !== "price") throw new Error(`Unsupported entity type on line ${index + 1}`);
    return value;
  });

  const ids = new Set<string>();
  for (const record of records) {
    if (ids.has(record.id)) throw new Error(`Duplicate record id: ${record.id}`);
    ids.add(record.id);
  }

  const summary = {batchId: args.batchId, records: records.length, target: "catalogueStaging/{batchId}/records", write: args.write};
  if (!args.write) {
    console.log(JSON.stringify({...summary, status: "dry_run"}, null, 2));
    return;
  }

  const emulatorHost = process.env.FIRESTORE_EMULATOR_HOST;
  if (!emulatorHost) throw new Error("Refusing write: FIRESTORE_EMULATOR_HOST must be set. This importer is emulator-only.");
  if (!process.env.GCLOUD_PROJECT && !process.env.FIREBASE_CONFIG) throw new Error("Set GCLOUD_PROJECT or FIREBASE_CONFIG for the emulator project.");
  if (!getApps().length) initializeApp({projectId: process.env.GCLOUD_PROJECT || "motivo-staging"});
  const db = getFirestore();
  const batchRef = db.collection("catalogueStaging").doc(args.batchId);
  const batch = db.batch();
  batch.set(batchRef, {
    batchId: args.batchId,
    status: "draft",
    recordCount: records.length,
    createdAt: new Date().toISOString(),
    target: "emulator",
    publicationPerformed: false
  }, {merge: false});

  for (let offset = 0; offset < records.length; offset += 450) {
    const chunk = records.slice(offset, offset + 450);
    const writeBatch = offset === 0 ? batch : db.batch();
    for (const record of chunk) {
      const docRef = batchRef.collection("records").doc(record.id);
      writeBatch.set(docRef, {...record, importBatchId: args.batchId, publicationStatus: "draft"}, {merge: false});
    }
    await writeBatch.commit();
  }
  console.log(JSON.stringify({...summary, status: "written_to_emulator", publicationPerformed: false}, null, 2));
}

main().catch((error: unknown) => {
  console.error(error instanceof Error ? error.message : error);
  process.exitCode = 1;
});

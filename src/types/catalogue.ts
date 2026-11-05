export type PublicationStatus = "draft" | "review" | "published" | "rejected";
export type FuelType = "petrol" | "diesel" | "cng" | "lpg" | "mild_hybrid" | "strong_hybrid" | "plug_in_hybrid" | "electric";
export type TransmissionType = "manual" | "amt" | "cvt" | "dct" | "torque_converter" | "single_speed" | "other";
export type BodyStyle = "hatchback" | "sedan" | "compact_suv" | "mid_size_suv" | "full_size_suv" | "mpv" | "muv" | "crossover" | "coupe" | "convertible" | "pickup" | "other";

export interface SourceReference {
  sourceId: string;
  url: string;
  retrievedAt: string;
  publishedAt?: string | null;
  licenceName?: string | null;
  attribution?: string | null;
}

export interface BrandRecord {
  id: string;
  name: string;
  aliases: string[];
  market: "IN";
  status: PublicationStatus;
  sourceRefs: SourceReference[];
  lastVerifiedAt: string;
}

export interface ModelRecord {
  id: string;
  brandId: string;
  name: string;
  generation?: string | null;
  modelYearStart?: number | null;
  modelYearEnd?: number | null;
  bodyStyle: BodyStyle;
  launchDate?: string | null;
  discontinuedDate?: string | null;
  status: PublicationStatus;
  sourceRefs: SourceReference[];
  lastVerifiedAt: string;
}

export interface VariantRecord {
  id: string;
  modelId: string;
  name: string;
  modelYear: number;
  fuel: FuelType;
  transmission: TransmissionType;
  drivetrain?: string | null;
  engineCode?: string | null;
  engineDisplacementCc?: number | null;
  batteryCapacityKwh?: number | null;
  motorPowerKw?: number | null;
  status: PublicationStatus;
  sourceRefs: SourceReference[];
  lastVerifiedAt: string;
}

export interface SourcedValue<T> {
  value: T | null;
  sourceRefs: SourceReference[];
  effectiveFrom?: string | null;
  effectiveTo?: string | null;
  lastVerifiedAt: string;
}

export interface VariantSpecifications {
  variantId: string;
  dimensionsMm?: {
    length?: SourcedValue<number>;
    width?: SourcedValue<number>;
    height?: SourcedValue<number>;
    wheelbase?: SourcedValue<number>;
    groundClearance?: SourcedValue<number>;
    bootSpaceLitres?: SourcedValue<number>;
  };
  performance?: {
    maxPowerPs?: SourcedValue<number>;
    maxTorqueNm?: SourcedValue<number>;
    claimedMileageKmpl?: SourcedValue<number>;
    claimedRangeKm?: SourcedValue<number>;
  };
  equipment?: Record<string, SourcedValue<boolean | string | number>>;
  warranty?: Record<string, SourcedValue<string | number>>;
}

export interface VehiclePriceRecord {
  id: string;
  variantId: string;
  market: "IN";
  stateCode: string;
  city?: string | null;
  rtoCode?: string | null;
  priceType: "ex_showroom" | "on_road";
  amountInr: number;
  breakdown?: {
    exShowroom?: number | null;
    roadTax?: number | null;
    registration?: number | null;
    insurance?: number | null;
    otherCharges?: number | null;
  };
  classification: "official" | "estimated" | "user_reported";
  effectiveDate: string;
  observedAt: string;
  sourceRefs: SourceReference[];
  lastVerifiedAt: string;
}

export interface SafetyRatingRecord {
  id: string;
  modelId: string;
  variantId?: string | null;
  agency: string;
  protocol: string;
  protocolVersion?: string | null;
  score?: number | null;
  maximumScore?: number | null;
  testDate: string;
  testedConfiguration?: string | null;
  applicabilityNotes: string;
  sourceRefs: SourceReference[];
  lastVerifiedAt: string;
}

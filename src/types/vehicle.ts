export type FuelType='Petrol'|'Diesel'|'CNG'|'Hybrid'|'Electric';
export type TransmissionType='Manual'|'AMT'|'CVT'|'DCT'|'Torque Converter'|'Automatic';
export type BodyStyle='Hatchback'|'Premium hatchback'|'Sedan'|'Compact SUV'|'Mid-size SUV'|'Full-size SUV'|'MPV'|'MUV'|'Crossover';
export interface Vehicle{id:string;brand:string;name:string;variant:string;bodyStyle:BodyStyle;fuel:FuelType;transmission:TransmissionType;priceLabel:string;priceLakhs:number;claimedMileage:string;realWorldMileage:string;engine:string;dataStatus:'demo';}

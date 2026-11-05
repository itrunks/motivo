import type {Vehicle} from '@/types/vehicle';

// Fictional sample records for testing filter and ranking behaviour only.
// Replace with researched, variant-specific Indian market data before public use.
export const demoVehicles:Vehicle[]=[
{id:'demo-1',brand:'Sample Motors',name:'City Hatch',variant:'Premium MT',bodyStyle:'Premium hatchback',fuel:'Petrol',transmission:'Manual',priceLabel:'₹9.2L*',priceLakhs:9.2,claimedMileage:'18.0 km/l*',realWorldMileage:'Not verified',engine:'1.2L petrol',dataStatus:'demo',priorityScores:{Safety:3,Mileage:4,Performance:3,Comfort:3,Features:4,Reliability:3,'Service cost':4,'Resale value':4,Space:2}},
{id:'demo-2',brand:'Sample Automotive',name:'Urban SUV',variant:'Plus MT',bodyStyle:'Compact SUV',fuel:'Petrol',transmission:'Manual',priceLabel:'₹11.4L*',priceLakhs:11.4,claimedMileage:'17.2 km/l*',realWorldMileage:'Not verified',engine:'1.0L turbo petrol',dataStatus:'demo',priorityScores:{Safety:4,Mileage:3,Performance:5,Comfort:4,Features:4,Reliability:3,'Service cost':3,'Resale value':3,Space:4}},
{id:'demo-3',brand:'Example Auto',name:'Tour Sedan',variant:'Select CVT',bodyStyle:'Sedan',fuel:'Petrol',transmission:'CVT',priceLabel:'₹12.1L*',priceLakhs:12.1,claimedMileage:'19.1 km/l*',realWorldMileage:'Not verified',engine:'1.5L petrol',dataStatus:'demo',priorityScores:{Safety:4,Mileage:4,Performance:3,Comfort:5,Features:4,Reliability:4,'Service cost':3,'Resale value':3,Space:4}},
{id:'demo-4',brand:'Sample Motors',name:'City Hatch CNG',variant:'CNG MT',bodyStyle:'Hatchback',fuel:'CNG',transmission:'Manual',priceLabel:'₹8.7L*',priceLakhs:8.7,claimedMileage:'27 km/kg*',realWorldMileage:'Not verified',engine:'1.2L petrol/CNG',dataStatus:'demo',priorityScores:{Safety:3,Mileage:5,Performance:2,Comfort:3,Features:2,Reliability:3,'Service cost':5,'Resale value':3,Space:2}}
];

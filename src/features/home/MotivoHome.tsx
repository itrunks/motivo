import {useMemo,useState} from 'react';
import {ScrollView,StyleSheet,Text,TouchableOpacity,View,useWindowDimensions} from 'react-native';
import {SafeAreaView} from 'react-native-safe-area-context';
import {Ionicons} from '@expo/vector-icons';
import {colors} from '@/theme/colors';
import {demoVehicles} from '@/data/vehicles';
import type {BodyStyle,FuelType,TransmissionType} from '@/types/vehicle';

const bodies:BodyStyle[]=['Hatchback','Premium hatchback','Sedan','Compact SUV','Mid-size SUV','Full-size SUV','MPV','MUV','Crossover'];
const fuels:Array<FuelType|'Any'>=['Any','Petrol','Diesel','CNG','Hybrid','Electric'];
const gearboxes:Array<TransmissionType|'Any'>=['Any','Manual','AMT','CVT','DCT','Torque Converter','Automatic'];
const priorities=['Safety','Mileage','Performance','Comfort','Features','Reliability','Service cost','Resale value','Space'];

export function MotivoHome(){
 const [budget,setBudget]=useState(15);
 const [fuel,setFuel]=useState<FuelType|'Any'>('Any');
 const [transmission,setTransmission]=useState<TransmissionType|'Any'>('Any');
 const [body,setBody]=useState<BodyStyle[]|'Any'>('Any');
 const [selectedPriorities,setSelectedPriorities]=useState<string[]>(['Safety','Mileage','Performance']);
 const {width}=useWindowDimensions();
 const wide=width>=960;
 const matches=useMemo(()=>demoVehicles.filter(v=>v.priceLakhs<=budget&&(fuel==='Any'||v.fuel===fuel)&&(transmission==='Any'||v.transmission===transmission)&&(body==='Any'||body.includes(v.bodyStyle))),[budget,fuel,transmission,body]);
 const toggleBody=(item:BodyStyle)=>setBody(current=>{const active=current==='Any'?[]:current;const next=active.includes(item)?active.filter(x=>x!==item):[...active,item];return next.length?next:'Any';});
 const togglePriority=(item:string)=>setSelectedPriorities(current=>current.includes(item)?current.filter(x=>x!==item):[...current,item]);
 return <SafeAreaView style={s.safe}><ScrollView contentContainerStyle={s.page}>
  <View style={s.nav}><View style={s.brand}><View style={s.logo}><Ionicons name="speedometer" size={19} color="#090b10"/></View><Text style={s.brandText}>motivo</Text></View><Text style={s.navCaption}>CAR RESEARCH, MADE CLEAR</Text></View>
  <View style={s.hero}><Text style={s.eyebrow}>THE CAR DECISION STUDIO</Text><Text style={s.heroTitle}>Find the car that{"\n"}fits your <Text style={{color:colors.accent}}>real life.</Text></Text><Text style={s.heroCopy}>Compare beyond brochures. Understand variant-level features, real-world mileage, safety and ownership before you decide.</Text><View style={s.heroFoot}><Text style={s.heroTag}>✓ Variant-first research</Text><Text style={s.heroTag}>✓ Evidence-led comparison</Text></View></View>
  <View style={[s.columns,wide&&s.columnsWide]}>
   <View style={[s.panel,wide&&{flex:1.1}]}>
    <Text style={s.eyebrow}>START WITH YOUR NEEDS</Text><Text style={s.heading}>Build your shortlist</Text>
    <Text style={s.field}>Your on-road budget</Text><View style={s.budgetRow}><Text style={s.budget}>{'₹'+budget+' lakh'}</Text><Text style={s.muted}>Maximum budget</Text></View>
    <View style={s.chips}>{[7,10,12,15,18,22,30].map(n=><Choice key={n} label={String(n)} active={budget===n} onPress={()=>setBudget(n)}/>)}</View>
    <Text style={s.field}>Fuel preference</Text><View style={s.chips}>{fuels.map(x=><Choice key={x} label={x} active={fuel===x} onPress={()=>setFuel(x)}/>)}</View>
    <Text style={s.field}>Transmission</Text><View style={s.chips}>{gearboxes.map(x=><Choice key={x} label={x} active={transmission===x} onPress={()=>setTransmission(x)}/>)}</View>
    <View style={s.fieldRow}><Text style={s.field}>Body style</Text><TouchableOpacity onPress={()=>setBody('Any')}><Text style={s.link}>Any type of car</Text></TouchableOpacity></View>
    <View style={s.chips}>{bodies.map(x=><Choice key={x} label={x} active={body==='Any'||body.includes(x)} onPress={()=>toggleBody(x)}/>)}</View>
    <Text style={s.field}>What matters most? <Text style={s.muted}>Select as many as you need</Text></Text>
    <View style={s.chips}>{priorities.map(x=><Choice key={x} label={x} active={selectedPriorities.includes(x)} onPress={()=>togglePriority(x)}/>)}</View>
    <View style={s.liveUpdate}><Ionicons name="flash" size={14} color={colors.accent}/><Text style={s.liveUpdateText}>Results update automatically when you change filters</Text></View>
    <Text style={s.disclaimer}>Preview uses fictional sample vehicles and illustrative figures, not verified market data.</Text>
   </View>
   <View style={[s.panel,s.results,wide&&{flex:0.9}]}>
    <Text style={s.eyebrow}>YOUR MATCHING GARAGE</Text><Text style={s.heading}>{matches.length+' matching cars'}</Text>
    {matches.length?matches.map(v=><View key={v.id} style={s.car}><View style={s.carTop}><View style={{flex:1}}><Text style={s.carBrand}>{v.brand}</Text><Text style={s.carName}>{v.name}</Text><Text style={s.muted}>{v.variant}</Text></View><Text style={s.price}>{v.priceLabel}</Text></View><View style={s.chips}><Tag label={v.bodyStyle}/><Tag label={v.fuel}/><Tag label={v.transmission}/></View><View style={s.rule}/><Info label="CLAIMED MILEAGE" value={v.claimedMileage}/><Info label="REAL-WORLD" value={v.realWorldMileage}/><Info label="ENGINE" value={v.engine}/><Text style={s.demo}>DEMO DATA · NOT VERIFIED</Text></View>):<View style={s.empty}><Text style={s.emptyTitle}>No demo matches</Text><Text style={s.mutedCenter}>Increase your budget or broaden the filters.</Text></View>}
   </View>
  </View>
  <View style={s.footer}><Text style={s.footerLogo}>motivo.</Text><Text style={s.muted}>Make the next car decision a better one.</Text><Text style={s.footerSmall}>RESEARCH FIRST. DECIDE WITH CONFIDENCE.</Text></View>
 </ScrollView></SafeAreaView>;
}
function Choice({label,active,onPress}:{label:string;active:boolean;onPress:()=>void}){return <TouchableOpacity onPress={onPress} style={[s.choice,active&&s.choiceActive]}><Text style={[s.choiceText,active&&{color:colors.accent}]}>{label}</Text>{active&&<Ionicons name="checkmark" size={12} color={colors.accent}/>}</TouchableOpacity>;}
function Tag({label}:{label:string}){return <View style={s.tag}><Text style={s.tagText}>{label}</Text></View>;}
function Info({label,value}:{label:string;value:string}){return <View style={s.info}><Text style={s.infoLabel}>{label}</Text><Text style={s.infoValue}>{value}</Text></View>;}
const s=StyleSheet.create({
 safe:{flex:1,backgroundColor:colors.background},page:{width:'100%',maxWidth:1440,alignSelf:'center',paddingHorizontal:24,paddingBottom:44},
 nav:{height:76,borderBottomWidth:1,borderBottomColor:colors.border,flexDirection:'row',alignItems:'center',justifyContent:'space-between'},
 brand:{flexDirection:'row',alignItems:'center',gap:10},logo:{width:35,height:35,borderRadius:11,backgroundColor:colors.accent,alignItems:'center',justifyContent:'center'},brandText:{fontSize:25,fontWeight:'900',color:colors.text,letterSpacing:-1},navCaption:{color:colors.muted,fontSize:9,letterSpacing:2,fontWeight:'800'},
 hero:{marginTop:26,padding:34,minHeight:270,backgroundColor:'#142019',borderRadius:22,borderWidth:1,borderColor:'#2b3c2d',justifyContent:'center'},
 eyebrow:{fontSize:9,color:colors.accent,fontWeight:'900',letterSpacing:2},heroTitle:{fontSize:48,lineHeight:54,fontWeight:'900',letterSpacing:-2,color:colors.text,marginTop:14},heroCopy:{fontSize:14,lineHeight:23,color:'#b5beca',maxWidth:620,marginTop:14},heroFoot:{flexDirection:'row',flexWrap:'wrap',gap:20,marginTop:22},heroTag:{fontSize:11,color:'#dce4dc',fontWeight:'700'},
 columns:{marginTop:22,gap:20},columnsWide:{flexDirection:'row',alignItems:'flex-start'},panel:{backgroundColor:colors.surface,borderRadius:19,borderWidth:1,borderColor:colors.border,padding:22},heading:{fontSize:22,fontWeight:'900',color:colors.text,marginTop:6,marginBottom:18},field:{fontSize:13,fontWeight:'800',color:colors.text,marginTop:19,marginBottom:10},fieldRow:{flexDirection:'row',alignItems:'center',justifyContent:'space-between'},budgetRow:{flexDirection:'row',alignItems:'baseline',justifyContent:'space-between'},budget:{fontSize:25,fontWeight:'900',color:colors.accent},muted:{fontSize:10,color:colors.muted},chips:{flexDirection:'row',flexWrap:'wrap',gap:7},choice:{minHeight:34,paddingHorizontal:10,borderRadius:9,borderWidth:1,borderColor:colors.border,backgroundColor:'#0d1118',flexDirection:'row',alignItems:'center',justifyContent:'center',gap:4},choiceActive:{borderColor:'#6d914a',backgroundColor:'#1b281b'},choiceText:{fontSize:10,fontWeight:'700',color:'#aab3c0'},link:{fontSize:10,fontWeight:'800',color:colors.accent},liveUpdate:{flexDirection:'row',alignItems:'center',gap:8,marginTop:22,padding:12,borderRadius:10,backgroundColor:'#1b281b',borderWidth:1,borderColor:'#344b2b'},liveUpdateText:{fontSize:10,color:'#d3e5c4',fontWeight:'600'},disclaimer:{fontSize:9,lineHeight:15,color:'#788291',textAlign:'center',marginTop:12},
 results:{minHeight:420},empty:{minHeight:300,alignItems:'center',justifyContent:'center',paddingHorizontal:15},emptyIcon:{height:70,width:70,borderRadius:22,backgroundColor:colors.accentDark,alignItems:'center',justifyContent:'center',marginBottom:17},emptyTitle:{fontSize:17,fontWeight:'900',color:colors.text,marginBottom:9},mutedCenter:{fontSize:11,lineHeight:19,color:colors.muted,textAlign:'center',maxWidth:270},car:{padding:14,borderRadius:13,backgroundColor:'#0c1118',borderWidth:1,borderColor:colors.border,marginBottom:11},carTop:{flexDirection:'row',justifyContent:'space-between',gap:8},carBrand:{fontSize:9,color:colors.muted,fontWeight:'800',letterSpacing:1},carName:{fontSize:17,color:colors.text,fontWeight:'900',marginTop:3},price:{fontSize:15,color:colors.accent,fontWeight:'900'},tag:{paddingVertical:5,paddingHorizontal:8,borderRadius:6,backgroundColor:colors.surfaceRaised},tagText:{fontSize:9,color:'#c3ccd7'},rule:{height:1,backgroundColor:colors.border,marginVertical:12},info:{flexDirection:'row',justifyContent:'space-between',gap:10,marginBottom:8},infoLabel:{fontSize:8,color:colors.muted,fontWeight:'900',letterSpacing:1},infoValue:{fontSize:10,color:colors.text,textAlign:'right',flexShrink:1},demo:{fontSize:8,color:'#d0ab62',fontWeight:'900',letterSpacing:1,marginTop:7},footer:{borderTopWidth:1,borderTopColor:colors.border,marginTop:32,paddingTop:22,alignItems:'center',gap:6},footerLogo:{fontSize:18,fontWeight:'900',color:colors.text},footerSmall:{fontSize:8,letterSpacing:1.5,color:'#697382',marginTop:8,fontWeight:'800'}
});

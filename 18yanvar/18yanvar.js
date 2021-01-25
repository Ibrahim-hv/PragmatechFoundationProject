
let ededler=[1,3,4,90,23,890,12,30,4,3,67,21]

// Bu massive gore asagidaki suallarin cavablarini tapan kod yazin

function Topla(a, b){
    return a + b;
}
function foo(value){
    return value %2 == 0;
}
function foo2(value){
    return value %2 == 1;
}


// 1 - Massivdeki ededlerin cemini tapan kod yazin
let Toplam=ededler.reduce(Topla);
console.log(Toplam);


// 2 - Massivdeki cut ededlerin cemini tapin
let cutEdedler=ededler.filter(foo);
let cutEdedlerinCemi=cutEdedler.reduce(Topla);
console.log(cutEdedlerinCemi);


// 3 - Massivdeki tek ededlerin cemini tapin
let tekEdedler=ededler.filter(foo2);
let tekEdedlerinCemi=tekEdedler.reduce(Topla);
console.log(tekEdedlerinCemi);


// 4 - Massivde tekrarlanan nece eded oldugunu tapin
function Tap(){
    let tekrarlananEdedler = [];
    let ededlerYeni=ededler.sort()
    for (let i = 0; i < ededlerYeni.length; i++) {
     if (ededlerYeni[i + 1] == ededlerYeni[i]) {
        tekrarlananEdedler.push(ededlerYeni[i]);
  }
}
    return tekrarlananEdedler
}
console.log(Tap().length +' / '+ Tap())    




// 5 Massivde nece eded ikireqemli eded oldugunu tapin
let ikireqemliler=0;
for(i=0;i<ededler.length;i++){
    if(String(ededler[i]).length==2){
        ikireqemliler++;
    }
    
}
console.log(ikireqemliler)



// 6 Massivdeki ededleri azalan sira ile ekrana yazdirin
function eksCixma(a,b){return b - a}
let azalanSira=ededler.sort(eksCixma);
console.log(azalanSira.join());


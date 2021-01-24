
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
console.log(Toplam)


// 2 - Massivdeki cut ededlerin cemini tapin

let cutEdedler=ededler.filter(foo);
let cutEdedlerinCemi=cutEdedler.reduce(Topla);
console.log(cutEdedlerinCemi)


// 3 - Massivdeki tek ededlerin cemini tapin

let tekEdedler=ededler.filter(foo2);
let tekEdedlerinCemi=tekEdedler.reduce(Topla);
console.log(tekEdedlerinCemi)


// 4 - Massivde tekrarlanan nece eded oldugunu tapin

// let tekrarlananEdedler
// console.log(tekrarlananEdedler)



// 5 Massivde nece eded ikireqemli eded oldugunu tapin



// 6 Massivdeki ededleri azalan sira ile ekrana yazdirin

function eksCixma(a, b){
    return b - a;
}
let azalanSira=ededler.sort(eksCixma)
console.log(azalanSira);


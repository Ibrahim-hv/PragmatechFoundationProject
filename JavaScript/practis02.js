let cars=[]
class Car{
    // yaradacaginiz obyektin 3 property-si var 
    // Name,Model,Price
    constructor(_name,_model,_price){
        this.Name=_name
        this.Model=_model
        this.Price=_price
    }
    
    // Car obyektinin butun detallarini gosteren metod yazin 
    showCarDetails(){
        let carDetails=`${this.Name} | ${this.Model} | ${this.Price}`
        console.log(carDetails)

    }

}

// 5 eded Car obyekti yaradin

let car01=new Car('X5','BMW',50000)
let car02=new Car('X6','BMW',70000)
let car03=new Car('Accent','Hundai',25000)
let car04=new Car('Sonata','Hundai',30000)
let car05=new Car('Samara','Lada',15000)


//  yaratdiginiz obyektleri cars adli arraye elave edin 
    // https://www.w3schools.com/jsref/jsref_obj_array.asp (Bu linkdeki metodlardan istifade edebilersiniz)
// 
cars.push(car01)
cars.push(car02)
cars.push(car03)
cars.push(car04)
cars.push(car05)

// asagidaki funsiyaya car adini yazdigimiz zaman ekrana o car haqqinda butun melumatlar gorunmelidir
function showCarByName(_carname){
    for(let i=0;i<cars.length;i++){
        if(cars[i].Name==_carname){
            cars[i].showCarDetails()
        }
    }
}
// parametr olaraq verilen deyerden daha bahali olan masinlarin siyahini gosteren funksiya yazin
function showCarsByPrice(_carprice){
    for(let i=0;i<cars.length;i++){
        if(cars[i].Price>_carprice){
            cars[i].showCarDetails()
        }
    }
}

function showCarsByModel(_modelname){
    for(let i=0;i<cars.length;i++){
        if(cars[i].Model==_modelname){
            cars[i].showCarDetails()
        }
    }
}
let charCount=0;
function countChar(_word,_char){
for(let i=0;i<_word.length;i++){
    if(_word[i]==_char){
        charCount++
    }
}
console.log(charCount)
}
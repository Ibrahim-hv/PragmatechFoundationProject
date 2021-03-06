let cars=[]
class Car{
    // yaradacaginiz obyektin 3 property-si var 
    // Name,Model,Price
    constructor(_name,_model,_price){
        this.Name=_name
        this.Model=_model
        this.Qiymet=_price
        
    }
    // Car obyektinin butun detallarini gosteren metod yazin 
    showCarDetails(){
        let carDetails=`${this.Name} | ${this.Model} | ${this.Qiymet}`
        console.log(carDetails)

    }
}

    let car01= new Car('Volvo','S8',120000);
    let car02= new Car('BMW','M3',13000);
    let car03= new Car('JEEP','Compas',37000);
    let car04= new Car('FIAT','Doblo',9700);
    let car05= new Car('LADA','Samara',4300);
// 5 eded Car obyekti yaradin
//  yaratdiginiz obyektleri cars adli arraye elave edin 
    // https://www.w3schools.com/jsref/jsref_obj_array.asp (Bu linkdeki metodlardan istifade edebilersiniz)
// 

cars.push(car01);
cars.push(car02);
cars.push(car03);
cars.push(car04);
cars.push(car05);

// asagidaki funsiyaya car adini yazdigimiz zaman ekrana o car haqqinda butun melumatlar gorunmelidir
function showCarByName(_carname){
   for(i=0;i<cars.length; i++){
       if(cars[i].Name==_carname)
       cars[i].showCarDetails()
   }
}


// parametr olaraq verilen deyerden daha bahali olan masinlarin siyahini gosteren funksiya yazin
function showCarsByPrice(_carprice){
    for(let i=0;i<cars.length;i++){
        if(cars[i].Qiymet>_carprice){
            cars[i].showCarDetails()
        }
    }
    
}



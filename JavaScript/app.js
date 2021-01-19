let cars=[]
class Car{
    // yaradacaginiz obyektin 3 property-si var 
    // Name,Model,Price
    constructor(_name, _model, _price){
        this.Name=_name
        this.Model=_model
        this.Qiymet=_price
        
    }
    // Car obyektinin butun detallarini gosteren metod yazin 
    showCarDetails(){
        console.log(this.Name + ' / ' + this.Model + ' / ' + this.Qiymet)
    }

}

    let car1= new Car('Volvo','S8', 120000);
    let car2= new Car('BMW', 'M3', 13000);
    let car3= new Car('JEEP', 'Compas', 37000);
    let car4= new Car('FIAT', 'Doblo', 9700);
    let car5= new Car('LADA', 'Samara', 4300);
// 5 eded Car obyekti yaradin
//  yaratdiginiz obyektleri cars adli arraye elave edin 
    // https://www.w3schools.com/jsref/jsref_obj_array.asp (Bu linkdeki metodlardan istifade edebilersiniz)
// 

cars.push(car1);
cars.push(car2);
cars.push(car3);
cars.push(car4);
cars.push(car5);

// asagidaki funsiyaya car adini yazdigimiz zaman ekrana o car haqqinda butun melumatlar gorunmelidir
function showCarByName(_carname){
   for(i=0;i<cars.length; i++){
       if(cars[i]==_carname)
       console.log(showCarDetails)
   }


// parametr olaraq verilen deyerden daha bahali olan masinlarin siyahini gosteren funksiya yazin
function showCarsByPrice(_carprice){

    
}



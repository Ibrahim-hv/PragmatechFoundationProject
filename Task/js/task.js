let container=document.createElement('div')
container.className='container'

let photo=document.createElement("img");
photo.setAttribute("src", "../img/1.jpg");
photo.setAttribute("alt", "The Lord of the Rings");

document.querySelector('#gallery').appendChild(container);

for(let rowCount=0;rowCount<2;rowCount++){
    let row=document.createElement('div')
    row.className='row'
    for(let colCount=0;colCount<3;colCount++){
        let col=document.createElement('div')
        col.className='col-4'

        let box=document.createElement('div')
        box.className='box'
        col.appendChild(box);
        row.appendChild(col);
    }
    container.appendChild(row);
    
}
function myFunc() {
    let x, i;
    x = document.querySelectorAll(".box");
    for (i = 0; i < x.length; i++) {
        x[0].style.background = "url('../img/1.jpg')";
        x[1].style.background = "url('../img/2.jpg')";
        x[2].style.background = "url('../img/3.jpg')";
        x[3].style.background = "url('../img/4.jpg')";
        x[4].style.background = "url('../img/5.jpg')";
        x[5].style.background = "url('../img/6.jpg')";
    }
}
myFunc()


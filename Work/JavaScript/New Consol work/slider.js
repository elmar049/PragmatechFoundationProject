let x = 0
let sliderMovement = document.querySelector('.slider-box')
let uzunluq = document.querySelector('.slider-container').clientWidth;
let item = document.querySelector('.slider-item');
item.style.width = `${uzunluq/3}px`;
let array = document.querySelectorAll('.slider-item');

for (let i = 0; i < array.length; i++) {
    array[i].style.width = `${uzunluq/3}px`
}




function left() {
    x = x + uzunluq / 3 + 20
    sliderMovement.style.left = `${x}px`
}

function right() {
    x = x - uzunluq / 3 + 20
    sliderMovement.style.left = `${x}px`
}
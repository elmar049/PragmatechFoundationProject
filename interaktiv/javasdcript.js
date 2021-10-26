let x = -10;

function upEle() {
    let buttonOne = document.querySelector('.box');
    buttonOne.style.transform = `translate(0px,${x}px)`
    x = x - 10



}
let y = 10

function downEle() {
    let buttonOne = document.querySelector('.box');
    buttonOne.style.transform = `translate(0px,${y}px)`
    y = y + 10
}


let c = -10

function leftEle() {
    let buttonOne = document.querySelector('.box');
    buttonOne.style.transform = `translate(${c}px,0px)`
    c = c - 10
}


function rightEle() {
    let buttonOne = document.querySelector('.box');
    buttonOne.style.transform = `translate(${x}px,0px)`
    x = x + 10
}
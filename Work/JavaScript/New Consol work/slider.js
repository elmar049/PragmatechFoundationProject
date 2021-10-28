let x = 0
let sliderMovement = document.querySelector('.slider-box')

function left() {
    x = x + 1220
    sliderMovement.style.left = `${x}px`
}

function right() {
    x = x - 1220
    sliderMovement.style.left = `${x}px`
}
let x = 400
let y = 400

// burda 400 oa goreki css dede beedi eyni noqteden bawlasin

let boxMovement = document.querySelector('.box')

function up() {
    y = y - 10
    boxMovement.style.top = `${y}px`
}

function down() {
    y = y + 10
    boxMovement.style.top = `${y}px`
}

function left() {
    x = x - 10
    boxMovement.style.left = `${x}px`
}

function right() {
    x = x + 10
    boxMovement.style.left = `${x}px`

}

function fun() {
    alert("salam")
}
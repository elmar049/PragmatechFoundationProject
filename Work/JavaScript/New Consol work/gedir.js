let y = 0
let box = document.querySelector('.box');

function gedir() {
    let winH = window.innerHeight;
    y = y + 20;
    box.style.top = `${y}px`;
    if (y > winH) {
        y = 0
    }
    console.log(y)
    setInterval(gedir, 100)
}
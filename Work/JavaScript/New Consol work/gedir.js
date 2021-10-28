let y = 0
let box = document.querySelector('.box');

function gedir() {
    y = y + 500;
    box.style.top = `${y}px`;

}

setInterval(gedir, 1000)
let metn = "We Love Programming and Elmar"
let txt = document.getElementById('22')
let i = 0;


setInterval(start, 200)

function start() {
    txt.innerText = metn.slice(0, i)
    i++;
    if (i > metn.length) {
        i = 1
    }
}
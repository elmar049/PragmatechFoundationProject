let cover = document.querySelector('.mainbox')
let textCover1 = document.querySelector('.text-first-cover')
let textCover2 = document.querySelector('.text-second-cover')

function leftCover() {
    cover.style.backgroundImage = 'URL("/static/uploads/cover.jpg")'

    textCover2.style.display = 'none'
    textCover1.style.display = 'block'

}

function rightCover() {
    cover.style.backgroundImage = 'URL("/static/uploads/cover2.jpg")'
    textCover1.style.display = 'none'
    textCover2.style.display = 'block'
}

let x = 0
let move = document.querySelector('.sliders')

function left() {
    x = x + 1200
    move.style.left = `${x}px`



}

function right() {
    x = x - 1200
    move.style.left = `${x}px`
    s

}
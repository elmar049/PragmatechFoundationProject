let cover = document.querySelector('.mainbox')
let textCover1 = document.querySelector('.text-first-cover')
let textCover2 = document.querySelector('.text-second-cover')

function leftCover() {
    cover.style.backgroundImage = 'URL("../images/cover.jpg")'

    textCover2.style.display = 'none'
    textCover1.style.display = 'block'

}

function rightCover() {
    cover.style.backgroundImage = 'URL("../images/cover2.jpg")'
    textCover1.style.display = 'none'
    textCover2.style.display = 'block'
}
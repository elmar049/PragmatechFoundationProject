function colorchange() {
    let x = document.querySelector('.box')
    let y = document.querySelector('h1')
    let R = Math.floor(Math.random() * 255)
    let G = Math.floor(Math.random() * 255)
    let B = Math.floor(Math.random() * 255)
    let color = "rgb(" + R + "," + G + "," + B + ")"
    x.style.backgroundColor = color
    y.innerHTML = color

}
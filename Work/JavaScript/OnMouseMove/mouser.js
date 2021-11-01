function Doit(event) {
    let x = event.clientX;
    let y = event.clientY;
    let colR = Math.floor(Math.random() * 255)
    let colG = Math.floor(Math.random() * 255)
    let colB = Math.floor(Math.random() * 255)
    let kar = document.createElement('div')
    kar.className = 'tezeshey'
    document.body.appendChild(kar);
    kar.style.top = `${y}px`;
    kar.style.left = `${x}px`;
    kar.style.backgroundColor = `rgb ( ${colR}, ${colG}, ${colB})`

    // let h = document.querySelector('.tezeshey')
    // h.style.top = `${y}px`
    // h.style.left = `${x}px`

}

//niye rengler emele gelmir?
ve men bunlar ucun yeniden bir
let yaratmaliyammi ? // yani men let h nese vermeliyemmi?
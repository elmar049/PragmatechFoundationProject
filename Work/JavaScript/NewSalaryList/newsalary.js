let maslar = [350, 400, 500, 480, 600, 1200, 4000, 520, 800, 270]

let yeni = []

//
for (let i = 0; i < maslar.length; i++) {
    if (maslar[i] < 500) {
        faiz = maslar[i] * 15 / 100
        maslar[i] = maslar[i] + faiz
        yeni.push(maslar[i])
    } else {
        yeni.push(maslar[i])
    }

}

console.log(yeni)
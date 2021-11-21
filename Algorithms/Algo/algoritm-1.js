let xx = 'Elmar Mammadov';
let yeni = '';
for (let i = 0; i < xx.length; i++) {
    if (xx[i] === xx[i].toLowerCase()) {
        yeni = yeni + xx[i].toUpperCase()
    } else {
        yeni = yeni + xx[i].toLowerCase()
    }
}

console.log(yeni)
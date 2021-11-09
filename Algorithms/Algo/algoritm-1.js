let x = 'Elmar Mammadov';
let yeni = '';
for (let i = 0; i < x.length; i++) {
    if (x[i] === x[i].toLowerCase()) {
        yeni = yeni + x[i].toUpperCase()
    } else {
        yeni = yeni + x[i].toLowerCase()
    }
}

console.log(yeni)
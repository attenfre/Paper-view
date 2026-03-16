const fs = require('fs');
const pdf = require('pdf-parse');

let dataBuffer = fs.readFileSync('public/pdfs/sn-article.pdf');

pdf(dataBuffer).then(function(data) {
    fs.writeFileSync('pdf_extracted.txt', data.text);
    console.log('Successfully extracted PDF to pdf_extracted.txt');
}).catch(console.error);

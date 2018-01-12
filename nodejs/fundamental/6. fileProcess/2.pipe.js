var fs = require('fs');
// zlib = lib to use gzip (*.gz format)
// and it's a builtin duplex stream
var zlib=require('zlib');

var readable=fs.createReadStream(__dirname+'/greet1.txt');

var writable=fs.createWriteStream(__dirname+'/greet2.txt');

var compressed=fs.createWriteStream(__dirname+'/greet.txt.gz')

// gzip = compressing stream = readable stream
var gzip=zlib.createGzip();

// same structure as readable.on()
// src.pipe(dest);
// and pipe returns dest;
readable.pipe(writable);

readable.pipe(gzip).pipe(compressed);

console.log(readable.isPaused())

// takeaway = streams and asynchronous than any other if possible
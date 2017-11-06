var fs = require('fs');

var readable=fs.createReadStream(__dirname+'/greet1.txt',
{encoding:'utf8',highWaterMark:1024});
// highWaterMark = bit size of buffer

// how stream and buffer work?
// == every custom stream is connected to EventEmitter,
// so on can be added
var writable=fs.createWriteStream(__dirname+'/greet2.txt');

// event-type 'data' means that 
// thru the stream 'readable' in every buffer filled up,
// stream emits and keep going on til finished
readable.on('data',function(chunk){
    console.log(chunk.length);
    writable.write(chunk);
});

// if stream is A, then i can B
// A        : B
// Readable = only read
// Writable = only write
// Duplex   = both
// Transform = change
// etc..
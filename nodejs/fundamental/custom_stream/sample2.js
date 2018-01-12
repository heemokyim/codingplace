const dupCtr = require('./customDuplex');
const readCtr=require('./customRead');
const writeCtr=require('./customWrite');

var dup = new dupCtr();
var read1= new readCtr();
var write1=new writeCtr();

// how it looks like
// Readable -> Duplex -> Writable

// order of execution
// 1. Read.read->Dup.write
// 2. Dup.read-> Write.write

read1.pipe(dup).pipe(write1);

read1.push('12345');
dup.push('hahaha');
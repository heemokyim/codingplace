// below takes 8 bytes as argument
var buffer = new ArrayBuffer(8);

// i'll use buffer as int32 array
var view = new Int32Array(buffer);
var view64=new Int16Array(buffer);

view[0]=5;
view[1]=15;

console.log(view);
console.log(view64);

// reason why there's no Int64?
// = because most 64 bit architecture is expanded from 32
// which means processing 32-bits twice in one tic.

// Int64Array can be shown in IA-64 architecture.

// and reason why platform matters?
// == NodeJS's core is C++ which is platform dependant


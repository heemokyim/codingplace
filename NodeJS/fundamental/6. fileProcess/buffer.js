// What to use to deal with binary data in NodeJS?
// = Buffer (has limited size)

// then why buffer exists in NodeJS?
// = No good way then Buffer to deal with binary

// utf8 is default
var buf = new Buffer('Hello','utf8');
// convert 'Hello' to binary data up to utf8 encoding

console.log(buf);
console.log(buf.toString());
console.log(buf.toJSON());
console.log(buf[2]);

// because buffer is finite, so does overwrite occur
buf.write('wo');
console.log(buf.toString());
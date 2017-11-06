var name = 'John Doe';

var greet = 'hello'+name;

// `` is called back-tick, or grave accent
// and used for template literal

// To use ``, we need converter like babeljs.io
// `hello ${name}` -> 'hello '+name
// and give it to the browser
var greet2 = `hello ${name}`;
// inside of curly braces, JS can exist
// only used in ES6

console.log(greet)
console.log(greet2)
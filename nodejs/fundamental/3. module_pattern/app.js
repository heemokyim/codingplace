var greet=require('./greet1')
greet()

var greet2=require('./greet2').greet
greet2()

// pointing same object 
// because it's the way require function does
// wrapped greet3.js only run once and cahing the result
var greet3=require('./greet3')
var greet3b=require('./greet3')
greet3.greet()
greet3b.greet()

// then how to point different object?
// == require function-constructor itself
var greet4=require('./greet4')
var grtr=new greet4();
var grtrb=new greet4();

var greet5=require('./greet5').greet
greet5()


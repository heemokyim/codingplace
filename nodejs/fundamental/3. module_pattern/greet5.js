var greeting="Hello world!!!!"

function greet(){
    console.log(greeting)
}

// below is called revealing module pattern
// only expose what you wanna show to outside
// protect contents 
module.exports={
    greet:greet
}
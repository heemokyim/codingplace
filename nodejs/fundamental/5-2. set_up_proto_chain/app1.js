var EventEmitter = require('events');
var util = require('util');

function Greetr(){
    this.greeting="Hello World!";
}

// make prototpye plugin between Greetr and EventEmitter
// so that they can access each other
// (connected thru prototype chain)
util.inherits(Greetr,EventEmitter)

Greetr.prototype.greet = function(data){
    console.log(this.greeting+" : "+data);
    this.emit('greet',data)
}

var greetr=new Greetr();

greetr.on('greet',function(data){
    console.log('someone greeted !' + data)
});

greetr.greet('woong')
var EventEmitter = require('events');
var util = require('util');

function Greetr(){
    // below is called super-constructor
    // constructor that i'm inheriting from
    EventEmitter.call(this);
    // this ensures any object from Greetr()
    // have features from super-constructor, EventEmitter
    this.greeting="Hello World!";
}

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
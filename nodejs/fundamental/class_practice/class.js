'use strict';

var eventEmitter=require('events');
var eventConfig=require('./config')

module.exports=class Person extends eventEmitter{
    constructor(name){
        super();
        this.name=name;
        this.eventType=eventConfig;
    }
    greet(){
        console.log(`hi my name is ${this.name}`)
        this.emit(this.eventType.GREET);
    }
}

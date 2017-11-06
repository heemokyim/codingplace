var eventEmitter=require('events');

var util=require('util');
util.inherits(Person,eventEmitter);

var eventConfig=require('./config');

function Person(first){
    eventEmitter.call(this)
    this.name=first,
    this.greet=function(){
        console.log(`hi my name is ${this.name}`)
        this.emit(eventConfig.GREET);
    }
}

var lee=new Person('lee');

lee.on(eventConfig.GREET,function(){
    console.log('finally we meet');
})

lee.greet();
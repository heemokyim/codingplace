// 'events' is builtin module, so no path-descriptor
var emitter=require('events');
var emtr=new emitter();

// after defining config, grasp them from config
// and then use safe variable to help debug easier
var eventConfig=require('./config').events;

emtr.on(eventConfig.GREET,function(){
    console.log('hi');
});
emtr.on(eventConfig.GREET,function(){
    console.log('wwow');
});

emtr.emit(eventConfig.GREET);
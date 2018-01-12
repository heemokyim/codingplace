var Emitter = require('./emitter');

var emtr = new Emitter();

//ex) event = greet, listener = responed to greet
// 1. map event and listener
emtr.on('greet',function(){
    console.log('somewhere, some said hello.')
});
emtr.on('greet',function(){
    console.log('A greeting occured!')
});

// 2. execute listener for proper event(=greet)
emtr.emit('greet');
'use strict';

var Person=require('./class')

var lee=new Person('lee');

lee.on(lee.eventType.GREET,function(){
    console.log('finally we meet');
})

lee.greet();
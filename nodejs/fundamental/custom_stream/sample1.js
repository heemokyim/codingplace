const readCtr=require('./customRead');
const writeCtr=require('./customWrite');

var read1=new readCtr();
var write1=new writeCtr();

// read1.pipe(write1); 
read1.on('data',function(data){
    write1.write(data,function(){
        console.log(`Writing '${data}' has been completed !`)
    });
    // this.pause();
})

//read1.resume();
read1.data.push('my name is lee');
read1.push('My name is lee');
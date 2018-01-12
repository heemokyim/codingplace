const rdStream = require('stream').Readable;
const util = require('util');

// stream.Readable == abstract class
// so that we need to implement .read()
function customRead(){
    rdStream.call(this);
    this.data=[];
    // readable.read(size)
    this._read=function(size){
        // Do what is supposed to do here.
        let chunk=this.data.shift();
        if (chunk!=null)
            this.push(chunk);
    }
}
util.inherits(customRead,rdStream);

module.exports=customRead;
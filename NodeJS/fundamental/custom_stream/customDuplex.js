const dupStream = require('stream').Duplex;
const util = require('util');

function customDuplex(){
    dupStream.call(this);
    this.data=[];

    this._read=function(size){
        //Do what it supposed to do here.
        let chunk=this.data.shift();
        if (chunk!=null)
            this.push(chunk);
    };

    this._write=function(chunk,encoding,callback){
        // Do what is supposed to do here.
        this.data.push(chunk);
        if(callback!=null){
            callback();
        }
    }
}

util.inherits(customDuplex,dupStream);

module.exports=customDuplex;
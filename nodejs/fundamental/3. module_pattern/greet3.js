function Greetr(){
    this.greeting="hello world!!!"
    this.greet=function(){
        console.log(this.greeting)
    }
}
// only run once
module.exports=new Greetr();
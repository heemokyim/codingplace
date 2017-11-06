function Greetr(){
    this.greeting="hello world!!!"
    this.greet=function(){
        console.log(greeting)
    }
}
// only run once
module.exports=Greetr;
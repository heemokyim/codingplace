// var a = 0;
//
// while(a<5){
//   a++;
//
//   if (a==3){
//     break
//   }
//   console.log(a)
// }
//
// while(a<5){
//   a++;
//
//   if(a==3){
//     continue
//   }
//   console.log(a)
// }
//
// for (var i =0; i<3;i++){
//   console.log(i)
// }
//

for(var i = 1; i<10; i++){
  for(var j= 1; j<10; j++){
    process.stdout.write(String(i)+"*"+String(j)+" = "+String(i*j)+" ")
  }
  console.log()
}

console.log()

for(var i = 1; i<10; i++){
  for(var j= 1; j<10; j++){
    process.stdout.write(String(j)+"*"+String(i)+" = "+String(j*i)+" ")
  }
  console.log()
}

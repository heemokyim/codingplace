function add(a,b,callback){
  var result = a+b
  callback(result)
}

function disp(data){
  console.log(data)
}

add(5,8,disp)

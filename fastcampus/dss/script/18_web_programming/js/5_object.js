var obj = {}
obj.math=92;
obj.eng=97;
obj.sci=85

console.log(obj)

for(var key in obj){
  console.log(key, obj[key])
}

console.log(obj.eng)
console.log(obj['eng'])

// 객체에 함수담기
var points = {
  'points':{'math':91, 'eng':86,'sci':95},
  'total':function(){
    var total =0
    for(var key in this.points){
      total += this.points[key]
    }
    return total;
  },
  'avg':function(){
    return this.total()/Object.keys(this.points).length;
  }
}

console.log(points.total());
console.log(points.avg());
console.log(points.avg().toFixed(2));

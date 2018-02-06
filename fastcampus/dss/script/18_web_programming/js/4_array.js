var arr = ['a','b','c','d','e']

console.log(arr)
console.log(arr.length)

// 뒤에 추가
arr.push('z')
console.log(arr)
// 앞에 추가
arr.unshift('y')
console.log(arr)

// 뒤에 삭제
arr.pop()
console.log(arr)
// 앞에 삭제
arr.shift()
console.log(arr)


// 역순으로 정렬 = a[:-1]
arr.reverse();
console.log(arr);
// 오름차순으로 정렬
arr.sort();
console.log(arr);

// 배열 자르기
arr.splice(2 , 1); // 2번에서 1개 자름
console.log(arr)
delete arr[2] // 데이터만 삭제, 공간은 남김
console.log(arr)

for(var i =0; i<arr.length;i++){
  console.log(arr[i]);
}

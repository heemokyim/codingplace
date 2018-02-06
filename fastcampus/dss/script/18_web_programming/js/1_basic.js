var TOTAL_COUNT = 50;
var firstName = 'Doojin';
var lastName = 'Park';
var dict = {'a': 1, 'b':2}

console.log(firstName,lastName,TOTAL_COUNT)
console.log(dict)

var i = 2;
i++;

console.log(i);

var c = 3;
var d = 4;
var result = (c-d)*5;

console.log(result);



// null, undefined, NaN
console.log(null);    // 값이 없음을 지정
console.log(undefined); // 값이 지정되지 않음
console.log(NaN);     // 존재하지 않는 데이터 형태 , 0/0같은


// == : 값만 비교, === : 타입까지 비교
console.log(1==1)
console.log(1=='1')

console.log(1===1)
console.log(1==='1')


// 논리연산자
console.log(true&&true)
console.log(true&&false)
console.log(false&&false)

console.log(true||true)
console.log(true||false)
console.log(false||false)


// 조건문
if(true){
  console.log('Hello Javascript')
}else{
  console.log('Hello Python')
}

if(false){
  console.log('hello javascript')
} else if(true){
  console.log('hello html')
} else {
  console.log('I really love python')
}

    // false 로 간주되는 데이터 형
if(null || undefined || NaN || 0|| ""){
  console.log('hello false')
}

    // true로 간주되는 데이터 형
if([] && {}){
  console.log('hello true')
}


// 점수를 입력하면 학점이 나오는 코드를 입력하시오

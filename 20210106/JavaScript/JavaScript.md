# JavaScript



## ES2015 (`ES6`)

- 자바스크립트의 고질적 문제들을 많이 해결한 ES2015를 지나 현재 ES2019까지 발표
- ES6라고 불리우는 이 버전은 기존 코드를 간결하게 작성할 수 있는 새로운 문법들이 추가 되면서 더욱 발전할 수 있는 계기가 되었음.





## Vanilla JS

- 크로스브라우징, 간편한 활용 등을 위해 많은 라이브러리 등장(대표적 jQuery)
- 최근 표준화된 브라우저, ES6이후의 다양한 도구의 등장으로 `순수 자바스크립트` 활용의 증대





## 브라우저에서 할 수 있는 일

- 전역 객체 window
  - DOM 조작
  - BOM 조작
    - navigator, screen, location, frames, history, XHR
  - JavaScript
    - Object, Array, Function





## JavaScript 기초



### 변수 선언

- 변수선언은 `var` 키워드를 활용해야 함.
- ES6 기준으로 아래와 같은 키워드가 등장함.
  - const
  - let





### 데이터 타임 분류 (`typeof`)

- 원시 타입(primitive) - 변경 불가능한 값(immutable)
  - boolean - true, false
  - null
  - undefined
  - number
  - string
  - symbol (ES6)
- 객체 타입 (object)
  - object : 일반 객체, function, array, date, RegExp





### Number

- 모든 숫자는 number 타입
- 8진수(0), 16진수(0x)로 표현 가능
- 추가적으로 infinity, -infinity, NaN(not a number)도 number 타입
- 상수
  - MDN 자바스크립트 number 참고





### String - 템플릿 문자열(ES6)

- 템플릿 문자열
  - 편하게 문자열 내에 변수를 사용 가능
  - 여러 라인으로 이뤄진 문자열 사용 가능





### null vs undefined

- null
  - 의도적으로 변수에 값이 없다는 것을 명시
  - typeof 출력시 object로 출력되는 것은 설계상의 실수
- undefined
  - 선언 이후 할당하지 않은 변수에 지정된 값
  - 자바스크립트 엔진이 할당 이전에 초기화된 값
  - 직접 값으로 할당해서 사용하는 것 금지





### 객체

- 자바스크립는 원시 타입을 제외하고는 모두 객체이다.
- 자바스크립트의 객체는 키와 값으로 구성된 속성의 집합이며, 프로퍼티 값이 함수일 경우 구분을 위해 메소드라고 부른다.





### 변수 유효 범위(scope)

- 자바스크립트는 함수 레벨 스코프를 가진다.
- 따라서 함수내에서 선언된 변수는 지역 변수이며, 나머지는 전역 변수로 활용된다.
- 변수 선언시 키워드를 쓰지 않으면, 암묵적 전역으로 설정된다.
  - 주의 : 변수가 아닌 전역객체의 프로퍼티로 생성
  - 따라서, delete로 지워지는 값





### 호이스팅과 let, const(ES6)

- 자바스크립트에서는 모든 선언을 호이스팅 한다.
- ES6에서 새롭게 등장한 let과 const 키워드는 이러한 내용을 방지한다.
  - 호이스팅 자체가 이뤄지지 않는 것은 아니고, var는 선언과 동시에 초기화를 하고, let, const는 선언과 초기화 단계가 분리되어 진행된다. 뿐만 아니라, 블록 레벨 스코프를 가지고 있다.







## JavaScript 문법



### == vs ===

- 동등 연산자 (==)
  - 값 비교 및 예상치 않은 변환
- 일치 연산자 (===)
  - 엄격한 같음. 형 비교





### 객체 생성 방법

- 객체는 Key와 Value로 구성된 속성들의 모임

- 기본 객체 생성법

  ```javascript
  var cat1 = {}
  var cat2 = {name: 'nerp', age: 3}
  // 객체 리터럴
  
  var dog1 = new Object()
  dog1.name = 'baduki'
  // Object 생성자 함수
  ```

- 객체 리터럴로 생성을 하는 경우 키가 문자열로 표기될 수 있다면, 암묵적 형변환이 발생한다.

- 그게 아닌 경우는 반드시 따옴표를 통해서 문자열로 만들어 주어야 한다.

  ```javascript
  var myObj = {
      name: 'lee',
      'e-mail': 'test@test.com'
  }
  ```

- 생성자 함수를 만들어 사용하면 마치 클래스처럼 속성이 동일한 객체를 생성할 수 있다.

  ```javascript
  function Person(name, age) {
      this.name = name;
      thi.age = age
  }
  
  var p1 = new Person('lee', 29)
  ```

- 속성 접근은 `.` 혹은 `[]`로 가능하다.

  - 단, 반드시 `[]`접근을 해야하는 경우가 있다

    ```javascript
    var myObj = {
        name: 'lee',
        'e-mail': 'test@test.com'
    }
    
    myObj.e-mail
    -> error
    
    myObj['e-mail']
    ```

    





### 배열 (Array)

- JS에서 배열은 값만 존재한다.

  ```javascript
  var a = [1, 2, 3]
  a
  {1, 2, 3}
  // 배열 리터럴
  
  var b = new Array(1, 2, 3)
  b
  {1, 2, 3}
  // Array 생성자 함수
  ```

  



### 배열 순회

```javascript
var a = [1, 2, 3]

for (var i = 0; i < a.length; i++) {
    console.log(i, a[i]);
}
0 1
1 2
2 3
// for


for (var elem of a) {
    console.log(elem)
}
1
2
3
// for .. of


a.forEach(function(elem, idx) {
    console.log(idx, elem)
})
0 1
1 2
2 3
// forEach

// for .. in 은 배열의 요소만 접근하는 것이 아니라 속성까지 출력될 수 있다.

a.name = 'lee'
a
{1, 2, 3, name: 'lee'}

for (var i in a) {
    console.log(i, a[i])
}
0 1
1 2
2 3
name lee

// for .. of 나 forEach에서는 아래와 같이만 출력된다. 
0 1
1 2
2 3

```







### 배열(Array) 메소드

- `sort` 메소드에 비교 함수(인자)가 없으면 문자열 기준으로 정렬한다.

- 비교함수가 있다면, 해당 함수의 리턴값이 0보다 크거나 작음으로 정렬한다.

  ```javascript
  var numbers = [4, 2, 5, 1, 3, 100]
  numbers.sort()
  console.log(numbers)
  [1, 100, 2, 3, 4, 5]
  
  numbers.sort(function(a, b) {
      return a - b;
  })
  console.log(numbers)
  [1, 2, 3, 4, 5, 100]
  ```

- 문자열 관련 - `join`, `toString`

  ```javascript
  var a = [1, 2, 3]
  a.join('-')
  "1-2-3"
  
  a.toString()
  "1,2,3"
  ```

- 배열 합치기 - `concat`

  ```javascript
  var a = [1, 2, 3]
  a.concat([4, 5])
  [1, 2, 3, 4, 5]
  
  a + [4, 5]
  "1,2,34,5"
  
  a.concat(4, 5)
  [1, 2, 3, 4, 5]
  ```

- 원소 삽입/삭제 `push`, `pop`, `unshift`, `shift`

  ```javascript
  var a = [1, 2, 3]
  undefined
  
  a.push(4)
  4
  a
  (4) [1, 2, 3, 4]
  
  a.pop(4)
  4
  a
  (3) [1, 2, 3]
  
  a.unshift(0)
  4
  a
  (4) [0, 1, 2, 3]
  
  a.shift(0)
  0
  a
  (3) [1, 2, 3]
  ```

- 인덱스 탐색 - `indexOf`

  ```javascript
  var a = [1, 2, 3]
  undefined
  
  a.indexOf(3)
  2
  a.indexOf(5)
  -1
  ```

- 배열 조작 `splice`

  ```javascript
  var a = [1, 2, 3]
  undefined
  
  a.splice(1, 2, '처음', '두번')
  (2) [2, 3]
  
  a
  (3) [1, "처음", "두번"]
  
  var a = [1, 2, 3]
  undefined
  
  a.splice(1, 2, '처음')
  (2) [2, 3]
  
  a
  (2) [1, "처음"]
  
  // 첫 번째는 시작 인덱스, 2번째는 제거할 요소의 수, 나머지는 추가할 요소이다
  ```

- 배열 자르기 `slice`

  ```javascript
  var a =[1, 2, 3]
  undefined
  
  a.slice(-2)
  (2) [2, 3]
  
  a.slice(1, 2)
  [2]
  
  a.slice(1)
  (2) [2, 3]
  
  a.slice()
  (3) [1, 2, 3]
  
  // 첫 번째는 시작 인덱스, 2번째는 종료할 기준 인덱스(입력값 전까지의)
  ```

  





### 함수 선언

```javascript
function sum(a, b) {
    return a + b;
}
// 함수 선언문

var sub = function(a, b) {
    return a - b;
}
// 함수 표현식

(function(a, b){return a * b})(1, 2)
2
// 즉시 실행 함수 
```





### 함수

- 화살표 함수 (ES6)

  ```javascript
  var sum = function(a, b) {
      return a + b;
  }
  
  var sum = (a, b) => {
      return a + b;
  }
  // {}는 한줄인경우엔 생략가능
  ```





### 함수 인자

- 자바스크립트에서는 함수는 매개변수 전달에 대한 제한이 없음
- arguments 객체는 매개변수로 넘겨진 모든 정보를 가지고 있음
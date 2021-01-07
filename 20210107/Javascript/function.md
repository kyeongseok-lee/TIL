## JavaScript Advanced Function



### 함수 호이스팅

- 자바스크립에서는 모든 선언이 호이스팅 된다.
- 함수 선언 방식의 가장 큰 차이점
  - 함수 선언문의 경우 선언, 초기화 할당이 모두 이뤄져 실행 가능
  - 함수 표현식은 변수 호이스팅이 발생하여, undefined. 즉, 실행불가





### Array helper methods

- forEach : 주어진 함수를배열의 요소 각각에 대해 실행
- filter : 주어진 함수를 배열의 요소 각각에 대해 실행하여 반환 값이 true인 요소를 모아 배열을 반환
- map : 주어진 함수를 배열의 요소 각각 에 대해 실행한 결과를 모아 배열을 반환
- every : 주어진 함수에 모든 요소가 true인 경우 true (boolean값을 반환)
- some : 주어진 함수에 하나라도 true인 경우 true (boolean 값을 반환)
- 이외에도 reduce, find 함수 등이 존재한다.







### First class function

- 자바스크립트 함수는 아래와 같은 특징을 가진다
  - 함수를 인자로 전달 가능함
  - 함수를 반환할 수 있음
  - 변수에 함수를 할당 가능함
- 위의 조건은 프로그래밍 언어에서의 일급 객체(first class object / first class citizen)의 조건이다.









### Closure

- 클로저는 함수와 함수가 선언된 어휘적 환경의 조합이다.

  ```javascript
  function count() {
      var cnt = 0
      return function() {
          cnt += 1
          return cnt
      }
  }
  
  var a = count()
  console.log(a())
  console.log(a())
  1
  2
  
  var b = count()
  console.log(b())
  console.log(b())
  1
  2
  
  // a는 count()의 return 값인 inner function인데 outter function인 count() 내부의 환경도 담아두고 있다.
  // b도 마찬가지다
  ```

  
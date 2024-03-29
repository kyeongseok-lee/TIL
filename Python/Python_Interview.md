# Python interview



- 파이썬의 주요 특징에 대해 이야기 해보세요

  >  파이썬은 인터프리터 언어이며, 동적 타이핑 언어입니다. 파이썬은 객체지향언어이고, 간결하고 단순하며 엄청난 커뮤니티의 지원을 받고 있다. 
  >
  > Garbage Collection 기능을 사용하여 필요할 때 메모리를 자동 할당하고 사용이 끝났을 때 자동으로 해제한다.
  >
  > 이미 만들어진 많은 수의 라이브러리를 제공한다.

  

- 파이썬에서 list와 tuple의 차이점에 대해 말해보세요

  > list는 데이터를 변경할 수 있고(가변적, mutable), tuple은 변경 할 수 없습니다.(불변적, immutable)



- 파이썬의 삼항연산자에 대해 설명하세요.

  > 일반적으로 자바스크립트와 같은 삼항연산자는 아니다. 파이썬의 삼항 연산자는 좀 더 영어 구문식 표현을 사용한다.

  ```python
  [true_value] if [condition] else [false_value]
  ```

  

- 리스트에서 음수 인덱스를 사용하면 어떻게 되나요?

  > 음수 인덱스를 사용할 시 가장 오른쪽 데이터를 기준으로 -1 이 첫번째 데이터가 되며, 오른쪽부터 검색을 시작한다.



- 변수나 함수 같은 식별자 길이의 제한이 있나요?

  > 공식적으로는 제한이 없는 걸로 알고 있습니다. 그렇지만 파이썬 스타일가이드인 PEP-8에서는 한줄 최대 약 80자 정도, PEP-20에서는 가독성이 중요하다고 표현한다. 따라서 너무 긴 식별자는PEP-8, PEP-20을 위반합니다.



- pass와 continue의 차이는 무엇인가요?

  > pass는 실행할 것이 아무 것도 없는 뜻을 의미한다. 따라서 아무런 동작을 하지 않고 다음 코드를 실행한다. 파이썬에서 함수 등을 작성할 때 반드시 무언가를 써야 문법적으로 오류가 발생하지 않기 때문에 이를 방지하는 역할로 사용할 수 있다. continue는 해당 위치에서 더 이상 진행하지 않고 다음 순서의 loop를 실행하게 합니다.
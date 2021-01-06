# DOM 및 이벤트



## DOM (Document Object Model)



### DOM

- **문서의 구조화된 표현을 제공**하여, DOM 구조에 접근 할 수 있는 방법을 제공
- 문서 구조, 스타일, 내용 등을 변결할 수 있도록 도우며, 구조화된 **노드와 오브젝트로 문서를 표현**
- 주요 객체
  - window:star: : DOM 문서를 표현하는 창. 가장 최상위 객체
  - document:star:: 페이지 콘텐츠의 진입점 역할을 하며, \<body> 등 다른 요소들을 포함
  - navigator, location, history, screen





### window

- window 객체는 전역 객체

- 다양한 함수, 이름공간, 객체 등이 포함

  ```javascript
  var test = 'test'
  undefined
  
  window.test
  "test"
  ```

  





### DOM 접근

- 단일 Node
  - document.getElementByID (id)
  - document.querySelector (selector) :star:
- HTMLCollection (live)
  - document.getElementsByTagName (Tag)
  - document.getElementsByClassName (class)

- NodeList (non-live)
  - document.querySelectorAll (selector) :star:

- HTMLCollection은 모두 live collection이며, 활용시 주의 를 요한다
- NodeList는 경우에 따라 live collection일 수 있다.





### DOM Node 기준 탐색 (우선 이런것도 있다 정도만 인지)

- parentNode, firstChild, lastChild
- Element
  - children
  - previousElementSibling, nextElementSibling
- 모든 요소
  - childNodes
  - prevSibling, nextSibling





### Node 생성 (이부분도 있다 정도)

- document.createElement(tagName) : 특정 태그를 생성
- document.createTextNode(text) : 텍스트 노드를 생성
- parentNode.appendChild(Node) : 마지막 자식 요소로 추가
- parentNode.removeChild(Node) : 해당 요소 제거 





### 

### innerHTML, insertAdjacentHTML

- DOM 조작시 아래와 같은 메서드를 통해서도 가능하나, **XSS 공격에 취약점**이 있으므로 사용시 주의
- element.innerHTML(text)
- element.insertAdjacentHTML(position, text)
  - position : beforebegin, afterbegin, beforeend, afterend











## JavaScript 이벤트



### Event

- 브라우저에서 특정한 이벤트가 발생하면 이에 대한 이후 행위를 정의할 수 있다.
- 이벤트를 정의하는 경우, 인라인으로도 작성 가능하나 분리하여 작성하는 것이 좋다
- 아래는 가능한 이벤트의 예시이다
  - load, copy, mouseover, click, submit 등





### addEventListener

- EventTarget.addEventListener(*type*, *listener*, [, *useCapture*])

  - type : 이벤트 유형

  - listener : 이벤트가 발생했들 때 실행할 콜백 함수 (핸들러)

  - useCapture : 기본 값(false), 상위 노드로 전파(버블링), 만약 true인 경우 하위 노드로 전파(캡처링)

    ```javascript
    const button = document.querySelector('button');
    button.addEventListener('click', function() {
        console.log('click');
    })
    ```

    



### 이벤트 전파

- Event는 해당 요소에서 전파되며, 캡처링(위에서 아래)과 버블링(아래에서 위)으로 구분된다.
- 항상 캡처링부터 시작하여 버블링으로 종료되며, addEventListener 메소드의 useCapture를 통해 특정 상황에 대하여 이벤트 관리가 가능하다.  (false가 기본값 -> bubbling, true -> capturing)







### 이벤트 객체

- 이벤트에 지정된 함수(핸들러)는 이벤트 객체를 매개변수로 받을 수 있다.
- 이벤트 객체에는 대표적으로 아래와 같은 속성과 메소드들이 있다
  - Event.target : 이벤트가 원래 발생하였던 대상
  - Event.currentTarget : 이벤트가 발생하였던 대상
  - Event.preventDefault() : 이벤트를 취소
  - Event.stopPropagation() : 이벤트 전파 중단





### 이벤트 객체와 this

- 이벤트 리스너의 콜백함수에서 this를 활용하는 경우, 이벤트 리스너에 바인딩 되어 있는 요소가 지정된다. 아래
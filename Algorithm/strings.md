# 문자열



## 문자의 표현



### 컴퓨터에서의 문자표현

- 글자 A를 메모리에 저장하는 방법에 대해서 생각해보자

- 물론 칼로 A라는 글자를 새기는 방식은 아닐 것이다. 메모리는 숫자만을 저장할 수 있기 때문에 A라는 글자의 모양 그대로 비트맵으로 저장하는 방법을 사용하지 않는 한(이 방법은 메모리 낭비가 심하다) 각 문자에 대해서 대응되는 숫자를 정해 놓고 이것을 메모리에 저장하는 방법이 사용될 것이다.

- 영어가 대소문자 합쳐서 52이므로 6(64)비트면 모두 표현할 수 있다. 이를 코드체계라고 한다.

  - 네트워크가 발전되기 저네 미국의 각 지역별로 코드체계를 정해 놓고 사용

  - 그렇지만, 네트워크가 발전하면서 서로간에 정보를 주고 받을 때 정보를 달리 해석한다는 문제가 생김
  - 그리하여, 혼동을 피하기 위해 `ASCII`라는 문자 인코딩 표준이 제정되었다.
  - ASCII는 7bit 인코딩으로 128문자를 표현하며 33개의 출력 불가능한 제어 문자들과 공백을 비롯한 95개개의 출력 가능한 문자들로 이루어져 있다.

- 그런데, 자국의 코드체계를 타 국가가 가지고 있지 않으면 정보를 잘못 해석 할 수 밖에 없었다.
- 그래서, 다국어 처리를 위해 표준을 만들었는데 이를 `유니코드`라고 한다.







### 문자의 분류

- 문자열(string)
  - fixed length
  - variable length
    - length controlled (java에서의 문자열)
    - delimited (c 언어에서의 문자열)





### Python에서의 문자열 처리

- 문자열은 시퀀스 자료형으로 분류되고, 시퀀스 자료형에서 사용할 수 있는 인덱싱, 슬라이싱 연산들을 사용할 수 있음

- 문자열 클래스에서 제공되는 메소드
  - replace(), split(), isalpha(), find()
- 문자열은 튜플과 같이 요소값을 변경할 수 없음(immutable)

- 유니코드(UTF-8)로 저장







### 문자열 뒤집기

- 자기 문자열에서 뒤집는 방법이 있고 새로운 빈 문자열을 만들어 소스의 뒤에서부터 읽어서 타겟에 쓰는 방법이 있겠다.
- 자기 문자열을 이용할 경우는 swap을 위한 임시 변수가 필요하며 반복 수행을 문자열 길이의 반만을 수행해야 한다.



### 문자열 비교, 대소, 정수 변환

```python
# 문자열 비교
arr = 'algorithm'
arr = list(arr)
N = len(arr)
for i in range(N//2):
    arr[i], arr[N-1-i] = arr[N-1-i], arr[i]
# print(arr) 


# 문자열 대소
# a < b --> a가 b보다 사전순으로 빠르다
# 문자열을 정렬 --> 사전순으로 정렬


# 문자열 숫자를 정수로 변환해서 저장
arr = '12345'
val = 0
for ch in arr:
    val = val * 10 + ord(ch) - ord('0')
# print(var)
```











## 패턴 매칭



### 패턴 매칭에 사용되는 알고리즘들

- 고지식한 패턴 검색 알고리즘
- 카프-라빈 알고리즘
- KMP 알고리즘
- 보이어-무어 알고리즘





### 고지식한 알고리즘(Brute Force)

- 본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 일일이 비교하는 방식으로 동작 

  ```python
  p = 'abcd'
  t = 'aasdfdabcdzatgwrtvaabcdadtwertabcderewa'
  
  n, m = len(t), len(p)
  i = j = 0
  while i < n:
      if t[i] != p[j]:
          i = i - j
          j = -1       
      
      i, j = i + 1, j + 1
      if j == m:
          print(i - j, t[i - j:])
          j = 0
  ```







### KMP 알고리즘

- 불일치가 발생한 텍스트 스트링의 앞 부분에 어떤 문자가 있는지를 미리 알고 있으므로, 불일치가 발생한 앞 부분에 대하여 다시 비교하지 않고 매칭을 수행
- 패턴을 전처리하여 배열 next[M]을 구해서 잘못된 시작을 최소화함
  - next[M]  :  불일치가 발생했을 경우 이동할 다음 위치
- 시간 복잡도 :  O(M+N)







### 보이어-무어 알고리즘

- 오른쪽에서 왼쪽으로 비교

- 대부분의 상용 소프트웨어에서 채택하고 있는 알고리즘

- 보이어-무어 알고리즘은 패턴에 오른쪽 끝에 있는 문자가 불일치하고 이 문자가 패턴 내에 존재하지 않는 경우, 이동 거리는 무려 패턴의 길이 만큼이 된다.

  ```python
  # 보이어-무어 호스풀 (간단한)
  
  p = 'abcd'
  t = 'aasdfdabcdzatgwrtvaabcdadtwertabcderewa'
  n, m = len(t), len(p)
  
  # skip 테이블 생성
  skip = [m] * 128    # a~z, A~Z
  
  for i in range(m-1):
      skip[ord(p[i])] = m - 1 - i
  
  i = 0
  while i <= n - m:
      for j in range(m - 1, -1, -1):
          if p[j] != t[i+j]:
              i += skip[ord(t[i+m-1])]
              break
      else:
          print(i, t[i:])
          i += m
  ```

  



### 문자열 매칭 알고리즘 비교

- 찾고자 하는 문자열 패턴의 길이 m, 총 문자열 길이 n
- 고지식한 패턴 검색 알고리즘 : 수행시간 O(mn)
- 카프-라빈 알고리즘 : 수행시간 O(n)

- KMP 알고리즘 : 수행시간 O(n)
- 보이어-무어 알고리즘
  - 앞의 두 매칭 알고리즘들의 공통점 텍스트 문자열의 문자를 적어도 한번씩 훑는다. 따라서 최선의 경우에도 O(n)
  - 보이어 무어 알고리즘은 텍스트 문자를 다 보지 않아도 된다.
  - 발상의 전환 : 패턴의 오른쪽부터 비교한다
  - 최악의 경우 수행시간 : O(mn)
  - 입력에 따라 다르지만 일반적으로 O(n) 보다 시간이 덜 든다
  - 최선 오메가(n/m)













































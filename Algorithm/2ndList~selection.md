## 2차원 배열



### 2차원 배열의 선언

- 1차원 List를 묶어놓은 List
- 2차원 이상의 다차원 List는 차원에 따라 index를 선언
- 2차원 List의 선언 : 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함
- Python에서는 데이터 초기화를 통해 변수선언과 초기화가 가능함



### 2차원 배열의 접근

```python
# i 행의 좌표
# j 열의 좌표

# arr => 2차원 배열

# 행 우선 순회
for i in range(len(arr)):
    for j in range(len(arr[0])):
        arr[i][j]
        

# 열 우선 순회
for j in range(len(arr[0])):
    for i in range(len(arr)):
        arr[i][j]
        
       
# 지그재그 순회
for i in range(len(arr)):
    for j in range(len(arr[0])):
        arr[i[j + (m-1-2*j) * (i % 2)]]
        # 방법은 여러가지다            
```

```python
# 델타를 이용한 2차 배열 탐색
# 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법

# 상 하 좌 우
# x: 행, y:열
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 튜플로 묶어서 사용도 가능
# diff = [(-1, 0), (1, 0), (0, -1), (0, 1)]

arr = [[]] # N * N

for x in range(N):
    for y in range(N):
        for d in range(4):
            tx, ty = x + dx[i], y + dy[i]
            # 항상 경계 체크 필요
            if 0 <= tx < N and 0 <= ty < N:
            # tx, ty에 대해서 작업을 한다.

```

```python
# 전치 행렬

# i, j = 행, 열
# arr -> N*N

for i in range(N):
    for j in range(N):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

1 2 3     1 4 7
4 5 6 ->  2 5 8 
7 8 9     3 6 9
```







### 부분집합 합문제

- 유한 개의 정수로 이루어진 집합이 있을 때, 이 집합의 부분집합 중에서 그 집합의 원소를 모두 더한 값이 0이 되는 경우가 있는지를 알아내는 문제
- 예들 들어, [-7, -3, -2, 5, 8] 이라는 집합이 있을 때, [-3, -2, 5]는 이 집합의 부분집합이면서 (-3) + (-2) + 5 = 0 이므로 이 경우의 답은 참이 된다.





### 비트 연산자

- 비트 연산자
  - `&` 비트 단위로 AND 연산
  - `|` 비트 단위로 OR 연산
  - `<<` 피연산자의 비트 열을 왼쪽으로 이동
  - `>>` 피연산자의 비트 열을 오른쪽으로 이동

- 1 << n : 2^n 원소의 개수가 n개인 부분집합수

-  i & (1<<j) : i의 j번째 비트가 1인지 확인

- 부분집합 생성 방법

  ```python
  arr = [3, 6, 7, 1, 5, 4]
  
  n = len(arr)
  
  for i in range(1 << n):
      for j in range(n):
          if i & (1 << j):
              print(arr[j], end=', ')
      print()
  print()
  ```

  





### 검색

- 저장되어 있는 자료 중에서 원하는 항목을 찾는 작업
- 목적하는 탐색 키를 가진 항목을 찾는 것
  - 탐색 키 (search key) : 자료를 구별하여 인식할 수 있는 키
- 검색의 종류
  - 순차 검색 `O(n)`
  - 이진 검색 `O(logn)`
  - 해쉬 `O(1)`





### 순차 검색

- 일렬로 되어 있는 자료를 순서대로 검색하는 방법
  - 가장 간단하고 직관적인 검색 방법
  - 배열이나 연결 리스트 등 순차구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용함
  - 알고리즘이 단순하여 구현이 쉽지만, 검색 대상의 수가 많은 경우에는 수행시간이 급격히 증가하여 비효율적임
- 2가지 경우
  - 정렬되어있는 경우
  - 정렬 되어 있지 않은 경우





### 이진 검색

- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
  - 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행함
- 이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다.
- 재귀 함수를 이용할 수 도 있다.





### 인덱스

- 인덱스라는 용어는 Database에서 유래했으며, 테이블에 대한 동작 속도를 높여주는 자료 구조를 일컫는다. Database 분야가 아닌 곳에서는 Look up table 등의 용어를 사용하기도 한다.
- 인덱스를 저장하는데 필요한 디스크 공간은 보통 테이블을 저장하는데 필요한 디스크 공간보다 작다. 왜냐하면 보통 인덱스는 키-필드만 갖고 있고, 테이블의 다른 세부 항목들은 갖고 있지 않기 때문이다.
- 배열을 사용한 인덱스
  - 대량의 데이터를 매번 정렬하면, 프로그램의 반응은 느려질 수 밖에 없다. 이러한 대량 데이터의 성능 저하 문제를 해결하기 위해 배열 인덱스를 사용할 수 있다.







### 선택 정렬

- 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식
- 정렬 과정
  - 주어진 리스트 중에서 최소값을 찾는다.
  - 그 값을 리스트의 맨 앞에 위치한 값과 교환한다.
  - 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복한다.
- 시간 복잡도
  - `O(n^2)`



### 셀렉션 알고리즘

- 저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법으르 셀렉션 알고리즘이라고 한다.
  - 최소값, 최대값 혹은 중간값을 찾는 알고리즘을 의미하기도 한다.
- 선택과정
  - 정렬 알고리즘을 이용하여 자료 정렬하기
  - 원하는 순서에 있는 원소 가져오기
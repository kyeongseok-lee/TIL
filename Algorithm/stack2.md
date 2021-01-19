# Stack 2



### 백트래킹

- 백트래킹 기법은 해를 찾는 도중에 막히면 (즉, 해가 아니면) 되돌아가서 다시 해를 찾아 가는 기법이다.
- 백트래킹 기법은 최적화 문제와 결정 문제를 해결할 수 있다.
- 결정 문제 : 문제의 조건을 만족하는 해가 존재하는지의 여부를 'yes' 또는 'no'가 답하는 문제
  - 미로 찾기
  - n-Queen 문제
  - Map coloring
  - 부분 집합의 합 문제 등



### 백트래킹과 깊이우선탐색과의 차이

- 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임(가지치기)
- 깊이우선탐색이 모든 경로를 추적하는데 비해 백트래킹은 불필요한 경로를 조기에 차단
- 깊이우선탐색을 가하기에는 경우의 수가 너무나 많음. 즉, N! 가지의 경우의 수를 가진 문제에 대해 깊이우선탐색을 가하면 당연히 처리 불가능한 문제
- 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 여전히 지수함수 시간을 요하므로 처리 불가능





### 백트래킹 기법

- 어떤 노드의 유망성을 점검한 후에 유망하지 않다고 결정되면 그 노드의 부모로 되돌아가 다음 자식 노드로 감
- 어떤 노드를 방문하였을 때 그노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 하며, 반대로 해답의 가능성이 있으면 유망하다고 한다.
- 가지치기 (pruning) : 유망하지 않는 노드가 포함되는 경로는 더 이상 고려하지 않는다.





### 부분집합 구하기

- 어떤 집합의 공집합과 자기 자신을 포함한 모든 부분집합을 powerset이라고 하며 구하고자 하는 어떤 집합의 원소 개수가 n일 경우 부분집합의 개수는 2^n이 나온다.
- 백트래킹 기법으로 powerset을 구해보자
  - 앞에서 설명한 일반적인 백트래킹 접근 방법을 이용한다.
  - n개의 원소가 들어있는 집합의 2^n개의 부분집합을 만들 때는 true 또는 false값을 가지는 항목들로 구성된 n개의 배열을 만드는 방법을 이용
  - 여기서 배열의 i번째 항목은 i번째의 원소가 부분집합의 값인지 아닌지를 나타내는 값이다.

```python
# 1
arr = 'ABC'
N = len(arr)
bit = [0] * N

for i in range(2):	# for 문을 N번 중첩
    bit[0] = i
    for i in range(2):
        bit[1] = i
        for i in range(2):
            bit[2] = i 
            for j in range(N):
                if bit[j]: print(arr[j], end='')
            print()

            
# 2 
def subset(k, n):	# K: 노드의 높이, n: 단말 노드의 높이
    if k == n:		# 종료 조건
        print(bit)
        for i in range(N):
            if bit[i]:
                print(arr[i], end='')
        print()
    else:
        bit[k] = 1	# k번 요소를 포함하는 선택
        subset(k + 1, n)
        bit[k] = 0	# k번 요소를 포함하지 않는 선택
        subset(k + 1, n)

subset(0, 3)
```





### 순열

```python
arr = 'ABC'
N = len(arr)

# 1
for i in range(N):              # 첫번째 요소 선택
    for j in range(N):          # 두번째 요소 선택
        if i != j:
            for k in range(N):  # 세번째 요소 선택
                if k != i and k != j:
                    print(arr[i], arr[j], arr[k])
          
        
        
# 2
order = []
for i in range(N):
    order.append(arr[i])                # 첫번째 요소 선택
    for j in range(N):          		# 두번째 요소 선택
        if arr[j] in order: continue
        order.append(arr[j])
        for k in range(N):  			# 세번째 요소 선택
            if arr[k] in order: continue
            order.append(arr[k])    
            print(order)
            order.pop()
        order.pop()
    order.pop()
    
    
    
# 3
visit = [0] * N
def perm(k, n):
    if k == n:
        print(order)
    else:
        for i in range(N):
            if visit[i]: continue
            visit[i] = 1
            order.append(arr[i])
            perm(k+1, n)
            visit[i] = 0
            order.pop()

perm(0, N)


# 4
def perm(k, n, visit):
    if k == n:
        print(order)
    else:
        for i in range(N):
            if visit & (1 << i): continue
            order.append(arr[i])
            perm(k+1, n, visit | (1 << i))
            order.pop()

perm(0, N, 0)
```





### N-Queen

```python
def possible(k, c): # k번 퀸의 위치는 (k, c)
    for i in range(k):
        if k-i == abs(c - col[i]):
            return True
    return False


def nQueen(k):
    global cnt
    if k == N:
        # 카운팅
        cnt += 1
        return
    else:
        for i in range(N):
            if v[i]: continue
            # 서로 대각에 위치하는지 판단
            # k번째 퀸의 열값을 i로 결정
            # 그 이전에 결정한 상태는 0 ~ k-1 번까지
            if possible(k, i): continue
            v[i] = 1
            col[k] = i
            nQueen(k + 1)
            v[i] = 0


for t in range(1, int(input()) + 1):
    N = int(input())
    
    col = [0] * N
    v = [0] * N
    cnt = 0
    nQueen(0)
    print(cnt)
```


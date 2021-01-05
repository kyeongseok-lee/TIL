def used_btr(k, n, f, sums):
    global min_s
    if k == n:
        if min_s > sums + btr[f][0]:
            min_s = sums + btr[f][0]
        return

    if sums > min_s:
        return
    
    for i in range(1, N):
        if v[i] == 0:
            v[i] = 1
            used_btr(k+1, n, i, sums + btr[f][i])
            v[i] = 0
           

import sys
sys.stdin = open('5189.txt', 'r')


for t in range(1, int(input()) + 1):
    N = int(input())
    btr = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * N
    min_s = 10000
    used_btr(0, N-1, 0, 0)
    print('#%d' % t, min_s)


'''
많은 방법이 있겠지만, 이 코드의 핵심은 재귀를 이용하여 
순열을 만들고, 처음 숫자를 0부터 시작하여 그 다음 숫자를 변수
f에 넣어 다음 재귀함수를 불러오면서 그 변수 f와 다음 숫자 i로 가는
배터리 값을 더해주는 방식이다. 또한 마지막은 다시 0으로 돌아와야 하기에
최소값 비교시에 마지막 숫자에서 0으로 가는 배터리 값을 더해서 비교하는 것이
핵심이다. 시간 단축을 위해서 중간에 이미 최소값보다 커버리면 return 해주도록
구성하였다.
'''
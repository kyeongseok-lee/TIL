from collections import deque
import sys
sys.stdin = open('5247.txt', 'r')


def bfs(s, e):
    q = deque()
    q.append(s)
    v[s] = 1
    while q:
        n = q.popleft()
        nums = [n+1, n-1, n*2, n-10]
        if e in nums:
            v[e] = v[n] + 1
            break
        for num in nums:
            if 1 <= num <= 1000000 and v[num] == 0:
                q.append(num)
                v[num] = v[n] + 1        
        

for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    v = [0] * 1000001
    bfs(N, M)
    print('#%d' % t, v[M] - 1)
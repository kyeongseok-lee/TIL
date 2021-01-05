from collections import deque

import sys
sys.stdin = open('5251.txt', 'r')

for t in range(1, int(input()) + 1):
    N, E = map(int, input().split())
    road = {i: [] for i in range(N+1)}
    
    for _ in range(E):
        s, e, w = map(int, input().split())
        road[s].append((e, w))
    
    q = deque()
    q.append(0)
    INF = float('inf')
    d = [INF] * (N+1)
    d[0] = 0
    while q:
        s = q.popleft()
        if s == N:
            continue
        for e, w in road[s]:
            if d[e] > d[s] + w:
                d[e] = d[s] + w
                q.append(e)

    print('#%d' % t, d)




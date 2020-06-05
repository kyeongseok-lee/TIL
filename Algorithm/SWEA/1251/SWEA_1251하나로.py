def distance(a, b):
    x1, y1 = xs[a], ys[a]
    x2, y2 = xs[b], ys[b]
    d = (x1-x2)**2 + (y1-y2)**2
    return d


import heapq
import sys
sys.stdin = open('1251.txt', 'r')


for t in range(1, int(input()) + 1):
    N = int(input())
    adj = {i: [] for i in range(N)}
    
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    ratio = float(input())

    INF = float('inf')
    key = [INF] * N
    mst = [0] * N
    q = []

    key[0] = 0
    heapq.heappush(q, (0, 0))

    while q:
        k, node = heapq.heappop(q)
        if mst[node]:
            continue
        mst[node] = 1
        for i in range(N):
            if i != node:
                if not mst[i] and key[i] > distance(node, i):
                    key[i] = distance(node, i)
                    heapq.heappush(q, (key[i],i))
    
    result = round(ratio * sum(key))
    print('#%d' % t, result)
    
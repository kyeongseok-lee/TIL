import sys
sys.stdin = open('5249.txt', 'r')

for t in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    lines = {i: [] for i in range(V+1)}
    for _ in range(E):
        s, e, c = map(int, input().split())
        lines[s].append([e, c])
        lines[e].append([s, c])

    
    INF = float('inf')
    W = [INF] * (V+1)
    mst = [0] * (V+1)

    W[0] = 0
    cnt = 0
    while cnt <= V:
        mins = INF
        u = -1
        for i in range(V+1):
            if not mst[i] and W[i] < mins:
                mins = W[i]
                u = i
        mst[u] = 1

        for n, wt in lines[u]:
            if not mst[n] and W[n] > wt:
                W[n] = wt
        cnt += 1
        
    print('#%d' % t, sum(W))
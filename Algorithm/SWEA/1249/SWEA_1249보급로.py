import sys
sys.stdin = open('1249.txt', 'r')


for t in range(1, int(input()) + 1):
    N = int(input())
    road = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            road[i][j] = int(road[i][j])
    
    INF = float('inf')
    dist = [[INF] * N for _ in range(N)]

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    dist[0][0] = 0
    q = [(0, 0)]
    while q:
        r, c = q.pop(0)
        
        for d in range(4):
            nr = r + dy[d]
            nc = c + dx[d]
            if 0 <= nr < N and 0 <= nc < N:
                if dist[nr][nc] > dist[r][c] + road[nr][nc]:
                    dist[nr][nc] = dist[r][c] + road[nr][nc]
                    q.append((nr, nc))

    print('#%d' % t, dist[N-1][N-1])


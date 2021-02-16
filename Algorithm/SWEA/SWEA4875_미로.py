def find_exit():
    sr, sc = 0, 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sr, sc = i, j
    
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    stack = [(sr, sc)]
    while stack:
        r, c = stack[-1]
        v[r][c] = 1
        for d in range(4):
            nr = r + dy[d]
            nc = c + dx[d]
            if 0 <= nr < N and 0 <= nc < N and v[nr][nc] == 0:
                if maze[nr][nc] == 3:
                    return 1
                elif maze[nr][nc] == 0:    
                    stack.append((nr, nc))
                    break
        else:
            stack.pop()
    return 0

for t in range(1, int(input()) + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    v = [[0] * N for _ in range(N)]
    
    result = find_exit()
    print('#%d' % t, result)

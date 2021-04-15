import sys
sys.stdin = open('a.txt', 'r')

N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * M for _ in range(N)]
direction = {
    0: [(0, -1, 3), (1, 0, 2), (0, 1, 1), (-1, 0, 0)],
    1: [(-1, 0, 0), (0, -1, 3), (1, 0, 2), (0, 1, 1)],
    2: [(0, 1, 1), (-1, 0, 0), (0, -1, 3), (1, 0, 2)],
    3: [(1, 0, 2), (0, 1, 1), (-1, 0, 0), (0, -1, 3)],
}

back = [(1, 0), (0, -1), (-1, 0), (0, 1)]

stack = [(r, c, d)]
cnt = 0
stop = False
while True:
    if stop:
        break
    r, c, d = stack[-1]
    if not v[r][c]:
        v[r][c] = 1
        cnt += 1    
    for dr in direction[d]:
        nr = r + dr[0]
        nc = c + dr[1]
        nd = dr[2]
        if board[nr][nc] == 0:
            if v[nr][nc] == 1:
                continue
            stack.append((nr, nc, nd))
            break
    else:
        nr = r + back[d][0]
        nc = c + back[d][1]
        if board[nr][nc] != 1:
            stack.append((nr, nc, d))
        else:
            stop = True
            
print(cnt)      
            


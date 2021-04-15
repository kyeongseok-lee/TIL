# 1 처음 푼 것
from itertools import combinations
import copy


N, M = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(N)]

zombi = []
safe = []

for i in range(len(lab)):
    for j in range(len(lab[i])):
        if lab[i][j] == 2:
            zombi.append((i, j))
        elif lab[i][j] == 0:
            safe.append((i, j))

safe_comb = list(combinations(safe, 3))

max_safe = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for i in range(len(safe_comb)):
    v = [[0] * M for _ in range(N)]
    lab_copy = copy.deepcopy(lab)
    zombi_copy = copy.deepcopy(zombi)
    safe_zone = len(safe) - 3
    for n in safe_comb[i]:
        lab_copy[n[0]][n[1]] = 1
    
    while zombi_copy:
        if safe_zone < max_safe:
            break
        r, c = zombi_copy.pop(0)
        v[r][c] = 1
        for d in range(4):
            nr = r + dy[d]
            nc = c + dx[d]
            if 0 <= nr < N and 0 <= nc < M and lab_copy[nr][nc] == 0:
                if v[nr][nc]:
                    continue
                v[nr][nc] = 1
                safe_zone -= 1
                zombi_copy.append((nr, nc))
    
    max_safe = max(safe_zone, max_safe)

print(max_safe)


#2 deque와 bfs 함수를 따로 만들고 쓸모없는 visit 배열을 없앴다.
from itertools import combinations
from collections import deque
import copy

def spread_zombi(zb, lc, result, max_safe):
    
    q = deque()
    q.extend(zb)
    
    while q:
        if max_safe > result:
            return max_safe
        r, c = q.popleft()
        for d in range(4):
            nr = r + dy[d]
            nc = c + dx[d]
            if 0 <= nr < N and 0 <= nc < M and lc[nr][nc] == 0:
                lc[nr][nc] = 2
                result -= 1
                q.append((nr, nc))
    
    return max(result, max_safe)



N, M = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(N)]

zombi = []
safe = []

for i in range(len(lab)):
    for j in range(len(lab[i])):
        if lab[i][j] == 2:
            zombi.append((i, j))
        elif lab[i][j] == 0:
            safe.append((i, j))

safe_comb = list(combinations(safe, 3))

max_safe = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for i in range(len(safe_comb)):
    lab_copy = copy.deepcopy(lab)
    safe_zone = len(safe) - 3
    for n in safe_comb[i]:
        lab_copy[n[0]][n[1]] = 1
    
    max_safe = spread_zombi(zombi, lab_copy, safe_zone, max_safe)
    
print(max_safe)

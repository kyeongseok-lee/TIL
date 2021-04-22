#1 pypy3로 통과, python 3 시간초과.. 
import copy

R, C, T = map(int, input().split())

dust = [list(map(int, input().split())) for _ in range(R)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

air_r1 = 0
for i in range(R):
    if dust[i][0] == -1:
        air_r1 = i
        break
air_r2 = air_r1 + 1

while T:
    after_dust = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if dust[i][j] == -1:
                after_dust[i][j] = -1
                continue
            if dust[i][j] > 0:
                cnt = 0
                for d in range(4):
                    r = i + dy[d]
                    c = j + dx[d]
                    if 0 <= r < R and 0 <= c < C and dust[r][c] != -1:
                        after_dust[r][c] += dust[i][j] // 5
                        cnt += 1
                after_dust[i][j] += dust[i][j] - dust[i][j] // 5 * cnt
    
             
    copy_dust = copy.deepcopy(after_dust)
    new = [[0] * C for _ in range(R)]
    for i in range(R):
        if i == 0 or i == R-1:
            copy_dust[i].pop(0)
            copy_dust[i].append(0)
        elif i == air_r1 or i == air_r2:
            copy_dust[i].pop()
            copy_dust[i].insert(1, 0)
        new[i] = copy_dust[i]

    for i in range(1, R-1):
        if i < air_r1:
            new[i][0] = after_dust[i-1][0]
        if i > air_r2:
            new[i][0] = after_dust[i+1][0]

    for i in range(R):
        if i < air_r1:
            new[i][C-1] = after_dust[i+1][C-1]
        if i > air_r2:
            new[i][C-1] = after_dust[i-1][C-1]            
    
    dust = copy.deepcopy(new)
    T -= 1


result = 0
for i in range(R):
    result += sum(dust[i])

print(result+2)


#2 아무리해도 python 3는 시간초과가 난다.
def spread():
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    after_dust = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if dust[i][j] >= 5:
                amount = dust[i][j] // 5
                cnt = 0
                for d in range(4):
                    r = i + dy[d]
                    c = j + dx[d]
                    if 0 <= r < R and 0 <= c < C and dust[r][c] != -1:
                        after_dust[r][c] += amount
                        cnt += 1
                dust[i][j] -= amount * cnt
    for i in range(R):
        for j in range(C):
            dust[i][j] += after_dust[i][j]


def rotate():
    
    for i in range(air_r1-1, 0, -1):
        dust[i][0] = dust[i-1][0]
    for i in range(C-1):
        dust[0][i] = dust[0][i+1]
    for i in range(air_r1):
        dust[i][C-1] = dust[i+1][C-1]
    for i in range(C-1, 1, -1):
        dust[air_r1][i] = dust[air_r1][i-1]
    dust[air_r1][1] = 0

    for i in range(air_r2+1, R-1):
        dust[i][0] = dust[i+1][0]
    for i in range(C-1):
        dust[R-1][i] = dust[R-1][i+1]
    for i in range(R-1, air_r2, -1):
        dust[i][C-1] = dust[i-1][C-1]
    for i in range(C-1, 1, -1):
        dust[air_r2][i] = dust[air_r2][i-1]
    dust[air_r2][1] = 0


R, C, T = map(int, input().split())

dust = [list(map(int, input().split())) for _ in range(R)]

air_r1 = 0
for i in range(R):
    if dust[i][0] == -1:
        air_r1 = i
        break
air_r2 = air_r1 + 1

for _ in range(T):
    spread()
    rotate()
         
result = 0
for i in range(R):
    result += sum(dust[i])
print(result + 2)

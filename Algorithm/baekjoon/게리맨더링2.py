#1 약간의 힌트를 받앗다
def sector_gap(r, c, d1, d2):
    sec_num = [[0] * N for _ in range(N)]
    sec_num[r][c] = 5
    for i in range(1, d1+1):
        sec_num[r+i][c-i] = 5
        sec_num[r+d2+i][c+d2-i] = 5
    for i in range(1, d2+1):
        sec_num[r+i][c+i] = 5
        sec_num[r+d1+i][c-d1+i] = 5
    
    sec_sum = [0] * 5
    for i in range(r+d1):
        for j in range(c+1):
            if sec_num[i][j] == 5:
                break
            sec_sum[0] += population[i][j]
    
    for i in range(r+d2+1):
        for j in range(N-1, c, -1):
            if sec_num[i][j] == 5:
                break
            sec_sum[1] += population[i][j]
    
    for i in range(r+d1, N):
        for j in range(c-d1+d2):
            if sec_num[i][j] == 5:
                break
            sec_sum[2] += population[i][j]
    
    for i in range(r+d2+1, N):
        for j in range(N-1, c-d1+d2-1, -1):
            if sec_num[i][j] == 5:
                break
            sec_sum[3] += population[i][j]
    
    sec_sum[4] = total - sum(sec_sum)

    return max(sec_sum) - min(sec_sum)

N = int(input())
population = [list(map(int, input().split())) for _ in range(N)]

total = 0
for i in range(N):
    total += sum(population[i])

answer = total        
xys = [(i, j) for i in range(N-2) for j in range(1, N-1)]
for xy in xys:
    r, c = xy
    for d1 in range(1, N):
        for d2 in range(1, N):
            if r + d1 + d2 >= N or c - d1 < 0 or c + d2 >= N:
                continue
            answer = min(answer, sector_gap(r, c, d1, d2))

print(answer)





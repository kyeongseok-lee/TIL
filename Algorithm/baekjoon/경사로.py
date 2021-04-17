def road_possible(r, L):
    v = [0] * len(r)
    cnt = 1
    for i in range(len(r)-1):
        if r[i] == r[i+1]:
            cnt += 1
            continue
        if abs(r[i] - r[i+1]) > 1:
            return 0

        if r[i] < r[i+1]:
            if cnt < L:
                return 0
            for j in range(i-L+1, i+1):
                if j < 0:
                    return 0
                if v[j]:
                    return 0   
                v[j] = 1

        else:
            for j in range(i+1, i+L+1):
                if j >= len(r):
                    return 0
                if v[j]:
                    return 0
                v[j] = 1

        cnt = 1
    
    return 1


N, L = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(N):
    result += road_possible(road[i], L)

for i in zip(*road):
    result += road_possible(i, L)

print(result)
# 1
for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    An = list(map(int, input().split()))
    Bn = list(map(int, input().split()))

    d = abs(N-M)
    if N > M:
        maxS = 0
        for i in range(M):
            maxS += An[i] * Bn[i]
        for i in range(1, d+1):
            S = 0
            newAn = An[i:i+M]
            for j in range(M):
                S += newAn[j] * Bn[j]
            if S > maxS:
                maxS = S
    else:
        maxS = 0
        for i in range(N):
            maxS += An[i] * Bn[i]
        for i in range(1, d+1):
            S = 0
            newBn = Bn[i:i+N]
            for j in range(N):
                S += An[j] * newBn[j]
            if S > maxS:
                maxS = S
    print('#%d' % t, maxS)


# 2
for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    An = list(map(int, input().split()))
    Bn = list(map(int, input().split()))

    d = abs(N-M)
    if N > M:
        maxS = 0
        for i in range(M):
            maxS += An[i] * Bn[i]
        for i in range(1, d+1):
            S = 0
            for j in range(M):
                S += An[i+j] * Bn[j]
            if S > maxS:
                maxS = S
    else:
        maxS = 0
        for i in range(N):
            maxS += An[i] * Bn[i]
        for i in range(1, d+1):
            S = 0
            for j in range(N):
                S += An[j] * Bn[i+j]
            if S > maxS:
                maxS = S
    print('#%d' % t, maxS)
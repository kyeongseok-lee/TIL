# 1
def chargeCnt(K, N, M):
    stop = [0] * (N+1)
    for i in range(M):
        stop[charge[i]] = 1
    cnt = 0
    i = 0
    while i < N:
        if i + K >= N:
            break
        if stop[i+K]:
            cnt += 1
            i += K
        else:
            newi = i
            for j in range(i+1, i+K):
                if stop[j]:
                    i = j
            if i == newi:
                return 0
            else:
                cnt += 1             
    return cnt
            

for t in range(1, int(input()) + 1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))

    result = chargeCnt(K, N, M)
    print('#%d' % t, result)


# 2
def chargeCnt(K, N, charge):
    charge.insert(0,0)
    charge.append(N)

    cnt = 0
    r_charge = 0
    for i in range(1, len(charge)):
        if charge[i-1] + K < charge[i]:
            return 0
        if r_charge + K < charge[i]:
            r_charge = charge[i-1]
            cnt += 1
    return cnt

for t in range(1, int(input()) + 1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))

    result = chargeCnt(K, N, charge)
    print('#%d' % t, result)

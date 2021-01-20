# 1
for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    maxS = 0
    minS = 10000 * M

    for i in range(N-M+1):
        S = 0
        for j in range(M):
            S += nums[i+j] 
        if S > maxS:
            maxS = S
        if S < minS:
            minS = S
    
    print('#%d' % t, maxS-minS)


# 2
for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    
    maxS = 0
    minS = 10000 * M
    
    for i in range(N-M+1):
        S = sum(nums[i:i+M])
        if S > maxS:
            maxS = S
        if S < minS:
            minS = S
    print('#%d' % t, maxS-minS)
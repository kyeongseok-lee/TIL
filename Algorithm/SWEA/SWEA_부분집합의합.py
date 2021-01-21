# 1
def comb(k, start, sums):
    global cnt
    if k == N:
        if sums == K:
            cnt += 1
        return

    for i in range(start, n):
        comb(k + 1, i + 1, sums + nums[i])
        

for t in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    nums = [n for n in range(1, 13)]
    pick = []
    n = len(nums)
    cnt = 0
    comb(0, 0, 0)
    print('#%d' % t, cnt)


# 2
for t in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    n = 12
    result = 0
    for i in range(1 << 12):
        sub_set = []
        cnt = 0
        for j in range(12):
            if i & (1 << j):
                sub_set.append(j+1)
                cnt += 1
        if cnt == N and sum(sub_set) == K:
            result += 1

    print('#%d' % t, result)
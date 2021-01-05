def dfs():
    global cnt

    for i in range(1, N+1):
        if v[i]:
            continue
        stack = [i]
        v[i] = 1
        while stack:
            f = stack[-1]
            for n in pairs[f]:
                if not v[n]:
                    stack.append(n)
                    v[n] = 1
                    break
            else:
                stack.pop()
        cnt += 1


import sys
sys.stdin = open('5248.txt', 'r')

for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    pairs = [[0] * (N+1) for _ in range(N+1)]
    v = [0] * (N+1)
    pairs = [[] for _ in range(N+1)]
    for i in range(0, len(nums), 2):
        s, e = nums[i], nums[i+1]
        pairs[s].append(e)
        pairs[e].append(s)  
    
    cnt = 0
    dfs()
    print('#%d' % t, cnt)
    

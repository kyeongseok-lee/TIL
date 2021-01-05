import sys
sys.stdin = open('1244.txt', 'r')


def reward(c, n):
    global cnt, ans, nums
    if c == cnt:
        if int(ltoi(n)) > ans:
            ans = int(ltoi(n))
        return

    if ltoi(n) in nums[c]:
        return
    
    nums[c].append(ltoi(n))

    for i in range(len(n)-1):
        for j in range(i+1, len(n)):
            n[i], n[j] = n[j], n[i]
            reward(c+1, n)
            n[i], n[j] = n[j], n[i]



def ltoi(l):
    return ''.join(l)


for t in range(1, int(input()) + 1):
    N, cnt = input().split()
    cnt = int(cnt)
    N = list(N)
    nums = [[] for _ in range(cnt+1)]
    ans = 0
    reward(0, N)
    print('#%d' % t, ans)
    



    

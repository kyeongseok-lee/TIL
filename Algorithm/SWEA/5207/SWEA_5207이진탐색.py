import sys
sys.stdin = open('5207.txt', 'r')


for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    A.sort()
    cnt = 0
    for b in B:
        l = 0
        r = len(A) - 1
        curr = 2
        prev = 0
        while l <= r:
            m = (l + r) // 2
            
            if prev == curr:
                break

            if A[m] == b:
                cnt += 1
                break
            
            elif A[m] < b:
                l = m + 1
                prev = curr
                curr = 1
            
            else:
                r = m - 1
                prev = curr
                curr = 0

    print('#%d' % t, cnt)
                 
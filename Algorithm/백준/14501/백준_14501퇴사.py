def max_profit(s, total):
    global max_total

    if s == N + 1:
        if total > max_total:
            max_total = total
        return

    for i in range(s, N+1):
        if i + (schedule[i][0] - 1) > N:
            continue
        max_profit(i + schedule[i][0], total + schedule[i][1])
            
    if total > max_total:
        max_total = total


import sys

sys.stdin = open('14501.txt', 'r')


for t in range(1, int(input()) + 1):
    N = int(input())
    
    schedule = [[0]]
    for _ in range(N):
        T, P = map(int, input().split())
        schedule.append([T, P])

    max_total = 0
    max_profit(1, 0)
    print('#%d' % t, max_total)
    

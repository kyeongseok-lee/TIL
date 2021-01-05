def find_minimum_cost(start, sums):
    global min_cost

    if start == N:
        if sums < min_cost:
            min_cost = sums
        return
    
    if sums > min_cost:
        return
    
    for i in range(N):
        if factory[i] == 1:
            continue
        factory[i] = 1
        find_minimum_cost(start + 1, sums + cost[start][i])
        factory[i] = 0


import sys
sys.stdin = open('5209.txt', 'r')


for t in range(1, int(input()) + 1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    factory = [0] * N
    min_cost = 100 * N

    find_minimum_cost(0, 0)
    print('#%d' % t, min_cost)
def min_charges(idx, gage, cnt):
    global min_charge
    gage -= 1
    if idx == N:
        if cnt < min_charge:
            min_charge = cnt
        return
    
    if cnt > min_charge:
        return
    
    min_charges(idx+1, stops[idx], cnt+1)

    if gage > 0:
        min_charges(idx+1, gage, cnt)
    

import sys
sys.stdin = open('5208.txt', 'r')


for t in range(1, int(input()) + 1):
    stops = list(map(int, input().split()))

    N = stops[0]
    min_charge = N
    min_charges(2, stops[1], 0)
    print('#%d' % t, min_charge)


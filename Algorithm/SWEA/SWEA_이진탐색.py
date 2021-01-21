def findPage(s, e, p):
    if s == p or e == p:
        return 0
    cnt = 0
    m = 0
    while m != p:
        m = (s+e) // 2
        if m < p:
            s = m
        else:
            e = m
        cnt += 1
    return cnt    

for t in range(1, int(input()) + 1):
    P, Pa, Pb = map(int, input().split())
    A = findPage(1, P, Pa)
    B = findPage(1, P, Pb)
    result = 0
    if A > B:
        result = 'B'
    elif A < B:
        result = 'A'
    else:
        result = 0
    print('#%d' % t, result)
        
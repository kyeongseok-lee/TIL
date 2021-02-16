def tournament(s, e):
    if s == e:
        return s
    
    else:
        center = (s+e) // 2
        m1 = tournament(s, center)
        m2 = tournament(center+1, e)

        if match_up[m1] == match_up[m2]:
            return m1
        elif match_up[m1] == 1:
            if match_up[m2] == 2:
                return m2
            else:
                return m1
        elif match_up[m1] == 2:
            if match_up[m2] == 3:
                return m2
            else:
                return m1
        elif match_up[m1] == 3:
            if match_up[m2] == 1:
                return m2
            else:
                return m1


for t in range(1, int(input()) + 1):
    N = int(input())
    match = list(map(int, input().split()))
    match_up = {i: match[i] for i in range(len(match))}
    
    result = tournament(0, N-1)
    print('#%d' % t, result+1)
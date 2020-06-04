import sys
sys.stdin = open('5521.txt', 'r')

for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    friends = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        friends[s].append(e)
        friends[e].append(s)

    v = [0] * (N+1)    
    
    q = [1]
    while q:
        f = q.pop(0)
        for i in friends[f]:
            if v[i] == 0:
                v[i] = v[f] + 1
                if v[i] < 2:
                    q.append(i)

    result = 0
    for i in range(N+1):
        if i != 1 and v[i] != 0:
            result += 1
    print('#%d' % t, result)
    

    
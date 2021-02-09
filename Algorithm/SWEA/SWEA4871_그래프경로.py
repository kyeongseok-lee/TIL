def find_node(s, e):
    stack = [s]
    while stack: 
        n = stack[-1]
        v[n] = 1
        for i in G[n]:
            if i == e:
                return 1
            else:
                if v[i] == 0:
                    stack.append(i)
                    break
        else:
            stack.pop()
    return 0


for t in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    v = [0] * (V + 1)

    for _ in range(E):
        s, e = map(int, input().split())
        G[s].append(e)
    
    rs, re = map(int, input().split())
    result = find_node(rs, re)
    print('#%d' % t, result)

    
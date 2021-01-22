def isPendul(r, c):
    for i in range(N-M+1):
        newr = r[i:i+M]
        newc = c[i:i+M]
        if newr == newr[::-1]:
            return newr
        if newc == newc[::-1]:
            return newc
    return 0
        
for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]

    result = 0
    k = 0
    while k < N:
        
        rlist = []
        clist = []
        for i in range(N):
            rlist.append(board[k][i])
            clist.append(board[i][k])
        
        result = isPendul(rlist, clist)
        if result:
            result = ''.join(result)
            break
        k += 1
            
    print('#%d' % t, result)
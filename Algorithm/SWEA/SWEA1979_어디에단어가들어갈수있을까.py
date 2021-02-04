for t in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    
    k = 0
    while k < N:

        for i in range(N-K+1):
            if board[k][i] == 1:
                if i-1 < 0 or board[k][i-1] == 0:
                    if i+K >= N or board[k][i+K] == 0:
                        r_cnt = 0
                        for j in range(i+1, i+K):
                            if board[k][j] == 1:
                                r_cnt += 1                
                        if r_cnt == K-1:
                            result += 1
                            
        for i in range(N-K+1):
            if board[i][k] == 1:
                if i-1 < 0 or board[i-1][k] == 0:
                    if i+K >= N or board[i+K][k] == 0:
                        c_cnt = 0
                        for j in range(i+1, i+K):
                            if board[j][k] == 1:
                                c_cnt += 1                
                        if c_cnt == K-1:
                            result += 1
    
        
        k += 1

    print('#%d' % t, result)           
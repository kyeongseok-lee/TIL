for t in range(1, int(input()) + 1):
    N = int(input())
    board = [[0] * 10 for _ in range(10)]
    cnt = 0
    for _ in range(N):
        rs, cs, re, ce, color = map(int, input().split())
        for i in range(rs, re+1):
            for j in range(cs, ce+1):
                board[i][j] += color
                if board[i][j] == 3:
                    cnt += 1
    
    print('#%d' % t, cnt)
    
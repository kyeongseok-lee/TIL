import copy

def find_n(n, board):
    for i in range(4):
        for j in range(4):
            if board[i][j][0] == n:
                return i, j
    return 0


def move_numbers(board): 
    for n in range(1, 17):
        if not find_n(n, board):
            continue
        i, j = find_n(n, board)
        d = board[i][j][1]
        cnt = 0
        while True:
            if cnt == 8:
                break
            ni = i + dy[d - 1]
            nj = j + dx[d - 1]
            if 0 <= ni < 4 and 0 <= nj < 4 and board[ni][nj][0] != -1:
                board[i][j] = (board[i][j][0], d)
                board[i][j], board[ni][nj] = board[ni][nj], board[i][j]
                break
            d = (d + 1) % 8
            cnt += 1

def move_shark(sr, sc, sd, feed, board):
    global max_feed
    if sr + dy[sd-1] < 0 or sr + dy[sd-1] >= 4 or sc + dx[sd-1] < 0 or sc + dx[sd-1] >= 4:
        max_feed = max(max_feed, feed)
        return
    
    move_numbers(board)
    for i in range(1, 4):
        nsr = sr + i * dy[sd-1]
        nsc = sc + i * dx[sd-1]
        if 0 <= nsr < 4 and 0 <= nsc < 4 and board[nsr][nsc][0]:
            cboard = copy_board(board) # copy.deepcopy()를 사용해도 상관없다.
            num = board[nsr][nsc][0]
            nsd = board[nsr][nsc][1]
            board[nsr][nsc] = (-1, nsd)
            board[sr][sc] = (0, 0)
            move_shark(nsr, nsc, nsd, feed + num, board)
            board = cboard
    else:
       max_feed = max(max_feed, feed)
       return


board = [[0] * 4 for _ in range(4)]

for i in range(4):
    fish = list(map(int, input().split()))
    board[i] = [(fish[i], fish[i+1]) for i in range(0, len(fish), 2)]

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

sr, sc = 0, 0
feed = board[sr][sc][0]
sd = board[sr][sc][1]
board[sr][sc] = (-1, sd)
max_feed = 0
move_shark(sr, sc, sd, feed, board)
print(max_feed)
                
                

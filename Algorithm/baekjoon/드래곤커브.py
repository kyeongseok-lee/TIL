#1 처음 리스트로 모으고 집합으로 중복제거 후 계산 
from itertools import combinations

import sys
sys.stdin = open('a.txt', 'r')

N = int(input())
direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]

xy = []
for _ in range(N):
    x, y, d, g = map(int, input().split())

    xy.append((y, x))
    xy.append((y+direction[d][0], x+direction[d][1]))

    ds = [d]
    while g:
        r, c = xy[-1]
        plus = []
        for i in range(len(ds)-1, -1, -1):
            dirs = (ds[i] + 1) % 4
            r += direction[dirs][0]
            c += direction[dirs][1]
            plus.append(dirs)
            xy.append((r, c))
        ds += plus
        g -= 1

kk = list(set(xy))
cnt = 0
for r, c in kk:
    if (r, c+1) in kk and (r+1, c) in kk and (r+1, c+1) in kk:
        cnt += 1
print(cnt)


#2 리스트 대신 2차원 배열에 1로 표시, 훨씬 시간이 단축됨
from itertools import combinations

import sys
sys.stdin = open('a.txt', 'r')

N = int(input())
direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]
board = [[0] * 101 for _ in range(101)]
for _ in range(N):
    x, y, d, g = map(int, input().split())

    board[y][x] = 1
    r = y+direction[d][0]
    c = x+direction[d][1]
    board[r][c] = 1
    
    ds = [d]
    while g:
        plus = []
        for i in range(len(ds)-1, -1, -1):
            dirs = (ds[i] + 1) % 4
            r += direction[dirs][0]
            c += direction[dirs][1]
            plus.append(dirs)
            board[r][c] = 1
        ds += plus
        g -= 1

cnt = 0
for i in range(100):
    for j in range(100):
        if board[i][j]:
            if board[i][j+1] and board[i+1][j] and board[i+1][j+1]:
                cnt += 1
print(cnt)
def start(k):
    n = []
    for i in range(R):
        for j in range(C):
            if cave[i][j] == k:
                n.append((i, j))
                
    return n


def waters():
    q = start('*')
    while q:
        r, c = q.pop(0)
        for d in range(4):
            nr = r + dy[d]
            nc = c + dx[d]
            if 0 <= nr < R and 0 <= nc < C and cave[nr][nc] == '.' and w[nr][nc] == 0:
                q.append((nr, nc))
                w[nr][nc] = w[r][c] + 1

    for i in range(R):
        for j in range(C):
            if cave[i][j] == 'D' or cave[i][j] == 'X':
                w[i][j] = R * C


def find_cave():
    q = start('S')
    while q:
        r, c = q.pop(0)
        for d in range(4):
            nr = r + dy[d]
            nc = c + dx[d]
            if 0 <= nr < R and 0 <= nc < C and (cave[nr][nc] == '.' or cave[nr][nc] == 'D') and v[nr][nc] == 0:
                if v[r][c] + 1 < w[nr][nc] or w[nr][nc] == 0: 
                    q.append((nr, nc))
                    v[nr][nc] = v[r][c] + 1


import sys
sys.stdin = open('3055.txt', 'r')


for t in range(1, int(input()) + 1):
    R, C = map(int, input().split())
    cave = [list(input()) for _ in range(R)]
    w = [[0] * C for _ in range(R)]
    v = [[0] * C for _ in range(R)]
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    waters()
    find_cave()
    final = start('D')
    fr, fc = final[0]

    print('#%d' % t, end=' ')
    if v[fr][fc]:
        print('%d' % v[fr][fc])
    else:
        print('KAKTUS')


'''
첫번 째로 시간에 따라 물이 되어버리는 칸을 BFS를 통해 구하고,
그에 따라 시작부터 굴까지 가는 최단 거리 BFS로 구한다.
두번의 BFS를 통해 각각 따로 구하는게 핵심이었다.
또한, 두번 째로는 처음 find_cave 함수를 구성할 때 2차원 배열 v를 통해 거리를 표시하는데 있어서
물에 의해 잠식된 칸을 시간으로 표현 해주었기에 현재 거리 + 1 보다 이후의 시간에
물이 되는 칸으로 이동할 수 있게 했었다. 그러나, 돌에 의해 막혀 있는 부분은 물에
잠식되지 않기에 계속 0이 되므로 조건을 하나 더 추가해 주어야 했다. 따라서 조건
v[r][c] + 1 < w[nr][nc] or w[nr][nc] == 0 이 핵심이었다.
'''
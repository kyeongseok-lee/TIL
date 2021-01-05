def double():
    for i in range(N):
        atom[i][0] += atom[i][0]
        atom[i][1] += atom[i][1] 


def energy_0():
    for i in range(N):
        if atom[i][3] != 0:
            return 0
    return 1


def move():
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for i in range(N):
        if atom[i][3] == 0:
            continue
        d = atom[i][2]  
        atom[i][0] += dx[d]
        atom[i][1] += dy[d]
         

import sys
sys.stdin = open('5648.txt', 'r')

for t in range(1, int(input()) + 1):
    N = int(input())
    atom = [list(map(int, input().split())) for _ in range(N)]
    double()
    S = 0
    time = 1
    while time <= 4000:
        if energy_0():
            break
        xys = {}
        move()
        for i in range(N):
            x, y = atom[i][0], atom[i][1]
            if abs(x) > 2000 or abs(y) > 2000 or atom[i][3] == 0:
                continue
            if (x, y) in xys.keys():
              S += atom[xys[(x, y)]][3] + atom[i][3]
              atom[xys[(x, y)]][3] = 0
              atom[i][3] = 0
            else:
                xys[(x, y)] = i
        time += 1
    print('#%d' % t, S)
import sys
sys.stdin = open('1247.txt', 'r')


def find_distance(k, n, s, sums):
    global min_distance    
    if k == n:
        sums += cal(s, home)
        if sums < min_distance:
            min_distance = sums
        return
    
    if sums > min_distance:
        return
    
    for i in range(n):
        if v[i]: continue
        v[i] = 1
        sums += cal(s, customer[i])
        find_distance(k+1, n, customer[i], sums)
        sums -= cal(s, customer[i])
        v[i] = 0


def cal(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def setting(l):
    xy = []
    for i in range(0, len(l), 2):
        xy.append([l[i], l[i+1]])
    return xy


for t in range(1, int(input()) + 1):
    N = int(input())
    xys = list(map(int, input().split()))
    company = [xys[0], xys[1]]
    home = [xys[2], xys[3]]
    customer = setting(xys[4:])
    v = [0] * N
    min_distance = 10000
    find_distance(0, N, company, 0)
    print('#%d' % t, min_distance)


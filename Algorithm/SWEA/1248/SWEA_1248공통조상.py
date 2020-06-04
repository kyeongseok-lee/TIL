import sys
sys.stdin = open('1248.txt', 'r')


def find_parent(n):
    l = []
    while adj[n][2] != 0:
        n = adj[n][2]
        l.append(n)
    return l


def our_parent(a, b):
    for i in a:
        for j in b:
            if i == j:
                return i


def my_childs(n):
    global cnt
    if n != 0:
        cnt += 1
        my_childs(adj[n][0])
        my_childs(adj[n][1])


for t in range(1, int(input()) + 1):
    V, E, a1, a2 = map(int, input().split())
    nums = list(map(int, input().split()))
    adj = [[0] * 3 for _ in range(V+1)]

    for i in range(0, len(nums), 2):
        s, e = nums[i], nums[i+1]
        if adj[s][0] == 0:
            adj[s][0] = e
        else:
            adj[s][1] = e
        adj[e][2] = s

    a1_l = find_parent(a1)
    a2_l = find_parent(a2)

    p = our_parent(a1_l, a2_l)

    cnt = 0
    my_childs(p)

    print('#%d' % t, p, cnt)

import sys
sys.stdin = open('1679.txt', 'r')


def bfs(n):
    q = []
    q.append(N)
    stop = 0
    while q:
        f = q.pop(0)
        nums = [f-1, f+1, f*2]
        if K in nums:
            v[K] = v[f] + 1
            break
        for num in nums:
            if num < 0 or num > 100000:
                continue
            if v[num] == 0:
                q.append(num)
                v[num] = v[f] + 1
                

N, K = map(int, input().split())
v = [0] * 1000000

if N == K:
    print(0)
else:
    bfs(N)
    print(v[K])        

'''
수빈이의 위치에서 갈 수 있는 경우의 수는 뒤로 한칸,
앞으로 한칸, 현재의 2배 위치로 이동, 총 3가지이다.
bfs를 이용하여 3가지 경우에 대해 너비우선탐색을 하였다.
방문배열을 만들어 방문하지 않은 위치에 대해서만 방문하여
현재 위치의 방문배열 값에 +1을 하여 시간을 표현하였다.
숫자가 0보다 작거나 100000을 넘어갈 때는 continue를 통해 스킵하는 것이 핵심
'''
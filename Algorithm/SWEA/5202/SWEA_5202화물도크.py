import sys
sys.stdin = open('5202.txt', 'r')

for t in range(1, int(input()) + 1):
    N = int(input())
    times = []
    for _ in range(N):
        s, e = map(int, input().split())
        times.append((s, e))
    
    times = sorted(times, key = lambda x : x[1] )
    
    f = times[0][1]
    cnt = 1

    for i in range(1, len(times)):
        if f <= times[i][0]:
            f = times[i][1]
            cnt += 1

    print('#%d' % t, cnt)


'''
핵심은 lambda식을 활용하여, times 리스트를 쉽게 활용할 수 있게
정렬을 한 것이다.
'''
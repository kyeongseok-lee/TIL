import sys
sys.stdin = open('5186.txt', 'r')


for t in range(1, int(input()) + 1):
    N = float(input())

    s = 0.5
    n = []
    overflow = 0
    while True:
        if len(n) >= 13:
            overflow = 1
            break
        if N == 0:
            break
        
        if N - s >= 0:
            n.append('1')
            N = N - s
        else:
            n.append('0')
        
        s = s / 2
    
    print('#%d' % t, end=' ')
    if overflow == 1:
        print('overflow')
    else:
        print(''.join(n))    


'''
5185_이진수 문제와 비슷한 문제인데, 소수를
이진수 변환해주는 문제다. 소수점 자리값 s를 0.5로
하고, 계속 2로 나누어주면 값을 줄였다. 그래서 주어진 N에서
s를 뺀 값이 0이상이면 n에 1을 넣었고, 아닌 경우 0을 넣었다.
N - s 가 0이상일때만 N의 값을 N - s로 줄여주는 것이 핵심이다.
'''
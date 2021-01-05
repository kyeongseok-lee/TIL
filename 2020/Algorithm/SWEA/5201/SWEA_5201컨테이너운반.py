import sys
sys.stdin = open('5201.txt', 'r')


for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))

    wi.sort(reverse=True)
    ti.sort(reverse=True)
    
    ws = ts = 0
    total_w = 0
    while True:
        
        if ws == len(wi) or ts == len(ti):
            break
        
        if wi[ws] <= ti[ts]:
            total_w += wi[ws]
            ws += 1
            ts += 1
        else:
            ws += 1
    
    print('#%d' % t, total_w)


'''
화물무게와 적재용량의 시작 인덱스를 0으로 동일하게 시작하여,
적재용량보다 같거나 적은 무게이면 총합 무게에 더해주고, 인덱스를 각각
1씩 더해준다. 그렇지 않으면 화물무게의 인덱스만 증가시켜주는게 핵심이다.
'''
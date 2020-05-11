def runs(x):
    cnt = 1
    k = sorted(x)
    for i in range(len(k)-1):
        if k[i] == k[i+1]:
            continue
        elif k[i] + 1 == k[i+1]:
            cnt += 1
        else:
            cnt = 1
        
        if cnt == 3:
            return 1
    
    return 0


def triplet(x):
    k =  list(set(x))
    for n1 in k:
        cnt = 0
        for n2 in x:
            if n1 == n2:
                cnt += 1
        if cnt == 3:
            return 1 
    
    return 0


def last(x):
    if x >= 1:
        return 1
    else:
        return 0


import sys
sys.stdin = open('5203.txt', 'r')


for t in range(1, int(input()) + 1):
    card = list(map(int, input().split()))
    
    p1 = []
    p2 = []
    for _ in range(2):
        c1 = card.pop(0)
        c2 = card.pop(0)
        p1.append(c1)
        p2.append(c2)        
    
    final = 0
    r1 = 0
    while card:
        p1.append(card.pop(0))
        result1 = last(runs(p1) + triplet(p1))

        if result1:
            final = 1
            break
    
        p2.append(card.pop(0))
        result2 = last(runs(p2) + triplet(p2))
        
        if result2:
            final = 2
            break
        
    print('#%d' % t, final)


'''
일반적인 베이비진 게임인데, 문제를 잘 못 이해했었다.
문제가 요구하는건 한번씩 카들를 가져가기에 먼저 가져간 사람이
런이나 트리플렛이면 이기는 방식이었다. 난 처음에 둘다 한장씩 받고
비교하는 방식으로 했기에 오류가 났다. 문제의 표현이 모호하기도 했던것 같다.
'''
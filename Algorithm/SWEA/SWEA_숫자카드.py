for t in range(1, int(input()) + 1):
    N = int(input())
    cards = list(map(int, input()))

    count = [0] * 10
    for i in range(N):
        count[cards[i]] += 1
    
    maxC = count[0]
    idx = 0
    for i in range(1, 10):
        if count[i] > maxC:
            maxC = count[i]
            idx = i
        if count[i] == maxC:
            if idx < i:
                idx = i
    print('#%d' % t, idx, maxC)
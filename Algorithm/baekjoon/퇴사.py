def find_max_profit(start, profit):
    global max_profit
    if start >= N:
        if profit > max_profit: 
            max_profit = profit
        return

    for i in range(start, N):
        t, p = tp[i]
        if i + t <= N:
            find_max_profit(i + t, profit + p)     
        else:
            find_max_profit(i + 1, profit)

N = int(input())
tp = []
v = [0] * N
for _ in range(N):
    T, P = map(int, input().split())
    tp.append((T, P))

max_profit = 0
find_max_profit(0, 0)
print(max_profit)
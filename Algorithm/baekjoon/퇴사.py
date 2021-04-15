# 내 풀이
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
for _ in range(N):
    T, P = map(int, input().split())
    tp.append((T, P))

max_profit = 0
find_max_profit(0, 0)
print(max_profit)


# 다른 사람 풀이 dp이용
# 1
n = int(input())

t, p = [0]*n, [0]*n

for i in range(n):
    t[i], p[i] = map(int, input().split())
        
dp = [0]*25

for i in range(n):
    if dp[i] > dp[i+1]: # 현재가 다음날보다 보상이 높다면
        dp[i+1] = dp[i] # 다음날 보상은 현재로
    if dp[i+t[i]] < dp[i] + p[i]: # T일 후에 받게될 금액이 상담을 해서 받게 될 금액에 현재 금액을 더한 금액보다 적다면
        dp[i+t[i]] = dp[i] + p[i] # 상담을 진행할 금액과 현재의 금액을 T일후에 받게 될 금액에 너어 저장
        
print(dp[n])

# 2
n = int(input())
T, P = [0 for i in range(n+1)], [0 for i in range(n+1)]
for i in range(n):
    a,b = map(int, input().split())
    T[i] = a
    P[i] = b
 
# dp[i]는 i번째날까지 일을 했을 때, 최대값이다. 
dp =[0 for i in range(n+1)]
 
for i in range(len(T)-1, -1, -1):      # 역순으로 진행
    if T[i]+i <= n:       # 날짜를 초과하지 않을 경우.
        dp[i] = max(P[i]+dp[i+T[i]], dp[i+1])   
    else:                 # 날짜를 초과할 경우.
        dp[i] = dp[i+1]
print(dp[0])

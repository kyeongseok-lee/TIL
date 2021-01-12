p = 'abcd'
t = 'aasdfdabcdzatgwrtvaabcdadtwertabcderewa'

n, m = len(t), len(p)

# find 함수 이용, 없으면 -1 반환
# idx = t.find(p)
# print(idx, t[idx:idx+m])

# idx = t.find(p, idx + m)
# print(idx, t[idx:idx+m])

# idx = t.find(p, idx + m)
# print(idx, t[idx:idx+m])

# idx = t.find(p, idx + m)
# print(idx, t[idx:idx+m])


# brute force
i = j = 0
while i < n:
    if t[i] != p[j]:
        i = i - j
        j = -1       
    
    i, j = i + 1, j + 1
    if j == m:
        print(i - j, t[i - j:])
        j = 0


N = 5
arr = [[0] * N for _ in range(N)]

rs = cs = 0
re = ce = N-1

cnt = 1
while rs <= re and cs <= ce:
    for i in range(cs, ce + 1):
        arr[rs][i] = cnt
        cnt += 1
    rs += 1

    for i in range(rs, re + 1):
        arr[i][ce] = cnt
        cnt += 1
    ce -= 1

    for i in range(ce, cs-1, -1):
        arr[re][i] = cnt
        cnt += 1
    re -= 1

    for i in range(re, rs - 1, -1):
        arr[i][cs] = cnt
        cnt += 1
    cs += 1


for i in range(len(arr)):
    print(arr[i])
p = 'abcd'
t = 'aasdfdabcdzatgwrtvaabcdadtwertabcderewa'
n, m = len(t), len(p)

# skip 테이블 생성
skip = [m] * 128    # a~z, A~Z

for i in range(m-1):
    skip[ord(p[i])] = m - 1 - i

i = 0
while i <= n - m:
    for j in range(m - 1, -1, -1):
        if p[j] != t[i+j]:
            i += skip[ord(t[i+m-1])]
            break
    else:
        print(i, t[i:])
        i += m
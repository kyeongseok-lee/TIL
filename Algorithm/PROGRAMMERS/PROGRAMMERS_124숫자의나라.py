# 1
# 미친짓, 심지어 효율성 0점... 생각을 잘못했다. 규칙을 찾아서 더하는 방식으로 하려고 했지만 효율이 너무 떨어졌다.
def solution(total):    
    n = ['1', '2', '4']
    if total < 4:
        return n[total-1]
    n_124 = [0] * (total + 1)
    n_124[1], n_124[2], n_124[3] = '1', '2', '4'

    pn = pg = 1
    cn = cg = 0
    ns = 3
    t = 2
    rpt = 3
    r = 0
    for i in range(4, total + 1):
        n_124[i] = n[r % 3] + n_124[pg]
        pg += 1
        cg += 1
        if cg == rpt:
            pg = pn
            cg = cn
            r += 1
        
        if i == ns + 3**t:
            pn = pg = pg + rpt 
            rpt = 3**t
            t += 1
            ns = i

    return n_124[total]

# 2
# 3진법을 이용하여, 재귀
def solution(n):
    if n <= 3:
        return '124'[n-1]
    else:
        n, r = divmod(n-1, 3)
        return solution(n) + '124'[r]    



# 3
# 3진법 이용, 반복
def solution(n):
    answer = ''
    while n:
        n, r = divmod(n, r)
        answer = '412'[r] + answer
        if r == 0:
            n -= 1
    return answer
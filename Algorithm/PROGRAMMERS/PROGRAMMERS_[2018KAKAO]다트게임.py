def solution(dart):
    ans = 0
    nums = [str(i) for i in range(11)]
    bonus = ['S', 'T', 'D']
    repo = {'S': 1, 'D': 2, 'T': 3, '*': 2, '#': -1}
    dart += '0'
    s = dart[0]
    darts = []
    for i in range(1, len(dart)):
        if dart[i] in nums and dart[i-1] not in nums:
            darts.append(s)
            s = ''
        s += dart[i]

    darts = darts[::-1]

    nxt = 0
    for s in darts:
        n = ''
        bonus_n = 0
        option_n = 1
        for m in s:
            if m in nums:
                n += m
            elif m in bonus:
                bonus_n = repo[m]
            else:
                option_n = repo[m]

        if nxt:
            if option_n != 1:
                ans += int(n)**bonus_n*option_n*2
                if option_n == -1:
                    nxt = 0
            else:
                ans += int(n)**bonus_n*2
                nxt = 0

        else:
            if option_n != 1:
                ans += int(n)**bonus_n*option_n
                if option_n == 2:
                    nxt = 1
            else:
                ans += int(n)**bonus_n

        if option_n == 2:
            nxt = 1
    return ans
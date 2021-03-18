def solution(s):
    answer = len(s)
    sln = (len(s) // 2) + 1

    for i in range(1, sln):
        cs = ns = 0
        ce = ne = i
        s_cnt = rpt = 0
        while True:
            ns += i
            ne += i
            if ne > len(s):
                if rpt:
                    s_cnt += i + len(str(rpt+1))
                    s_cnt += len(s) - (ne - i)
                else:
                    s_cnt += len(s) - cs
                break
            
            if s[cs:ce] != s[ns:ne]:
                if rpt:
                    s_cnt += i + len(str(rpt+1)) 
                else:
                    s_cnt += i
                rpt = 0    
                cs, ce = ns, ne
            else:
                rpt += 1
    
        if s_cnt < answer:
            answer = s_cnt

    return answer


# 처음에 rpt: 일때 s_cnt += i + 1로 해주어서 오류가 발생했다.
# 반복이 1자리수로 반복될 때는 문제가 없지만 그 이상 발생할 경우 반복횟수만큼 더해주어야 했기에,
# rpt를 문자열로 바꿔서 더해주어야 했다. 2번 반복시 rpt는 1이므로 실제 반복 횟수보다 rpt값이 1 작았기 때문에,
# 최종적으로 rpt + 1을 문자열로 바꿔서 그 길이 만큼 더해주어야 한다.
            


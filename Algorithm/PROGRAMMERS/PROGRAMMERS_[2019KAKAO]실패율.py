# 1
def solution(N, stages):
    answer = []
    num = len(stages)
    for i in range(1, N+1):
        if num != 0:
            cnt = stages.count(i)
            answer.append((i, cnt/num))
            num -= cnt
        else:
            answer.append((i, 0))

    answer.sort(key=lambda x:(-x[1], x[0]))
    return [i[0] for i in answer]

# 2 dict 사용
def solution(N, stages):
    answer = {}
    num = len(stages)
    for i in range(1, N+1):
        if num != 0:
            cnt = stages.count(i)
            answer[i] = cnt / num
            num -= cnt
        else:
            answer[i] = 0

    answer = sorted(answer, key=lambda x:(-answer[x], x))
    return answer





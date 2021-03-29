def min_distance(name, cur):
    min_dis, nxt = len(name), 0

    for i in range(len(name)):
        if i == 0 and name[i] != 'A':
            return (0, 0)
        
        if name[i] == 'A':
            continue
        if cur > i:
            dis_1 = cur - i
            dis_2 = i + len(name) - cur
            choice = min(dis_1, dis_2)
            if choice < min_dis:
                min_dis = choice
                nxt = i
        else: 
            dis_1 = i - cur
            dis_2 = cur + len(name) - i
            choice = min(dis_1, dis_2)
            if choice < min_dis:
                min_dis = choice
                nxt = i

    return (min_dis, nxt)

def solution(name):
    answer = 0
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha_value = {alpha[i]: i for i in range(len(alpha))}
    name = list(name)
    
    not_A = 0
    for n in name:
        if n != 'A':
            not_A += 1

    cur = 0
    while not_A:

        result = min_distance(name, cur)
        cur = int(result[1])
        answer += result[0]

        al_1 = alpha_value[name[cur]]
        al_2 = len(alpha_value) - alpha_value[name[cur]]
        if al_1 > al_2:
            answer += al_2
        else:
            answer += al_1
        not_A -= 1
        name[cur] = 'A'
        
    return answer



# 논란의 오류가 있다. 나중에 다시 풀어보길...
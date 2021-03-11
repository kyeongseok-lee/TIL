# 1 내 풀이
def solution(skill, skill_trees):
    answer = 0
    order = dict()
    for i in range(len(skill)):
        order[skill[i]] = i
    
    for skt in skill_trees:
        skt = list(skt)
        stack = []
        cnt = 0
        ln = len(skt)
        while skt:
            s = skt.pop(0)
            n = order.get(s)
            if n is None:
                stack.append(s)
            
            elif cnt == n:
                stack.append(s)
                cnt += 1
            else:
                break
        if  len(stack) == ln:
            answer += 1

    return answer


# 2 다른 사람 풀이
def solution(skill,skill_tree):
    answer=0
    for i in skill_tree:
        skillist=''
        for z in i:
            if z in skill:
                skillist+=z
        if skillist==skill[0:len(skillist)]:
            answer+=1
    return answer



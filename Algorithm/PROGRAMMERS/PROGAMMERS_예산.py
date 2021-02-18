def solution(d, budget):
    answer = 0
    d.sort()
    total = 0
    for i in d:
        if total + i > budget:
            break
        total += i
        answer += 1
    
    return answer


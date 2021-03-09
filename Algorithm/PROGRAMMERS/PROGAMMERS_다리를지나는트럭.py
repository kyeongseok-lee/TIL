# 1 
def sum_list(lst):
    result = 0
    for i in lst:
        result += i[0]
    return result

def solution(bridge_length, weight, truck_weights):
    answer = 0
    acrossing = []
    v = [0] * len(truck_weights)
    i = 0
    while acrossing or truck_weights:
        for n in acrossing:
            v[n[1]] += 1  
        for n in acrossing:
            if v[n[1]] == bridge_length:
                acrossing.remove(n)
        if truck_weights != [] and sum_list(acrossing) + truck_weights[0] <= weight:
            n = truck_weights.pop(0)
            acrossing.append((n, i))
            i += 1
        answer += 1

    return answer


# 2
def solution(bridge_length, weight, truck_weights):
    answer = 0
    acrossing = []
    total_w = 0
    while acrossing or truck_weights:
        
        if acrossing and answer - acrossing[0][1] == bridge_length:
            n, t = acrossing.pop(0)
            total_w -= n  

        if truck_weights and total_w + truck_weights[0] <= weight:
            n = truck_weights.pop(0)
            acrossing.append((n, answer))
            total_w += n
        answer += 1

    return answer



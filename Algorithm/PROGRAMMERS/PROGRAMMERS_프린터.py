def solution(priorities, location):

    golden = [(i, priorities[i]) for i in range(len(priorities))]
    order = []
    
    while golden:
        idx, prt = golden.pop(0)
        if golden:
            if max(golden, key=lambda x: x[1])[1] <= prt:
                order.append(idx)
            else:
                golden.append((idx, prt))
        else:
            order.append(idx)

    for i in range(len(order)):
        if order[i] == location:
            return i + 1

    

# 1 시간초과가 많이 낫다. 사실 수학 공식대로 풀지 않으면 시간 초과가 나는거 같다...
answer = 0
def comb(start, clothes, pick):
    global answer
    if len(pick) >= 2:
        answer += 1
        

    for i in range(start, len(clothes)):
        if clothes[i][1] in pick:
            continue
        pick.append(clothes[i][1])
        comb(i+1, clothes, pick)
        pick.pop()
        
    
def solution(clothes):
    comb(0, clothes, [])
    return answer + len(clothes)


# 2 수학 공식이다. 단순히 생각하면 각 항목을 다 곱한 값을 이야기 할 수 있지만 그건 "하나씩은 반드시 포함되는 경우"로 계산된다.
# 따라서 포함되지 않았을 때도 고려해야 함으로 각 항목+1 을 곱해줘야한다.
# 마지막으로 최소 한가지는 착용해야 하므로 아무것도 착용하지 않았을 경우인 1을 빼주어야 최종 답이 나온다.
def solution(clothes):
    answer = 1
    dic = dict()

    for cloth, Type in clothes:
        if dic.get(Type):
            dic[Type] += 1
        else:
            dic[Type] = 1    

    for Type in dic:
        answer *= (dic[Type] + 1)

    return answer - 1

# Counter와 reduce를 활용하여 쉽게 했다.
# reduce는 함수, 변수, 초기값 형태로 작동한다.
def solution(clothes):
    from collections import Counter
    from functools import reduce
    kk = [kind for name, kind in clothes]
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return cnt.values()





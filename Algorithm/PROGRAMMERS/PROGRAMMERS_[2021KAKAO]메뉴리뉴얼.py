# 1 내 풀이
def comb(k, start, r, n, alphas, pick, result):
    if k == r:
        if result.get(pick):
            result[pick] += 1
        else:
            result[pick] = 1
        return
    
    for i in range(start, n):
        pick += alphas[i]
        comb(k+1, i+1, r, n, alphas, pick, result)
        pick = pick[:-1]
    
    return result

def solution(orders, course):
    answer = []

    for i in course: 
        comb_cnt = dict()
        for order in orders:
            result = comb(0, 0, i, len(order), sorted(order), '', comb_cnt)
        if not comb_cnt:
            continue
        max_num = max(comb_cnt.values())
        if max_num < 2:
            continue
        for key in comb_cnt.keys():
            if comb_cnt[key] == max_num:
                answer.append(key)   
    answer.sort()
    return answer


# 2 라이브러리 사용 다른 사람 풀이
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for size in course:
        order_comb = []
        for order in orders:
            order_comb += combinations(sorted(order), size)
        most_ordered = Counter(order_comb).most_common()
        answer += [alpha for alpha, cnt in most_ordered if cnt > 1 and cnt == most_ordered[0][1]]
    return [''.join(alpha) for alpha in sorted(answer)]


# 처음에는 너무 이상하게 접근해서 오류와 시간초과가 많이 났다. 그래서 조합만 쓰는 힌트를 얻어서 구현했다.
# 주의했던 점은 i가 order의 길이보다 크면 comb_cnt가 빈 딕셔너리가 된다. 그래서 continue 처리해주었다.
# 또한, 최소 2명이상의 고객이 선택해야하니 max_num이 2보다 작으면 continue 처리해주었다.
# 마지막에 정렬해서 리턴해주었다

# itertools의 combination으로 조합을 손쉽게 구현할 수 있다. 라이브러리 쓰는 습관이 안되어 있었는데 신세계다...
# 그리고 collections의 Counter를 이용하여 배열안에 데이터가 몇번 나왔는지 딕셔너리로 리턴해준다.
# 마지막으로 Counter의 most_common() 매서드를 이용하여 데이터가 많은 순으로 정렬된 배열을 리턴받는다.
# 유용한 라이브러리인거 같다.
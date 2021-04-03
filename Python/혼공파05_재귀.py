# 리스트 평탄화 재귀
def flatten(data):
    result = []
    for i in data:
        if type(i) == list:
            result += flatten(i)
        else:
            result += [i]
    return result




# 한 테이블에 앉을 수 있는 최소, 최대 인원이 주어지고, 전체 인원을 테이블에 배치 할 수 있는 방법 재귀
# 테이블은 제한이 없음. 따라서 
memo = {}
min_sitted = 2
max_sttted = 10
def grouping(people, sitted):
    key = str([people, sitted])

    if memo.get(key):
        return memo[key]

    if people < 0:
        return 0

    if people == 0:
        return 1

    cnt = 0
    for i in range(sitted, max_sttted + 1):
        cnt += grouping(people - i, i)

    memo[key] = cnt

    return cnt

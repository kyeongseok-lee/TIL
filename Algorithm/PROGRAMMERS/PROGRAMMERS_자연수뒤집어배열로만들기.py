# 1
def solution(n):
    answer = list(str(n))
    for i in range(len(answer)):
        answer[i] = int(answer[i])
    answer = answer[::-1]
    return answer

# 2
def solution(n):
    return list(map(int, str(n)))[::-1]
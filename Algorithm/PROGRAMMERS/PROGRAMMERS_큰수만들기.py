def max_num(num):
    mn = ('0', '-1')
    for i in range(len(num)):
        if num[i] > mn[1]:
            mn = (i, num[i])
        if num[i] == '9':
            break
    return mn[0] 
       
def solution(number, k):
    answer = ''
    n = len(number)
    rm = k
    while len(answer) < n-k:
       new = number[:rm+1]
       idx = max_num(new)
       answer += new[idx]
       number = number[idx+1:]
       rm -= idx
    return answer

# 처음에 재귀로 풀었는데 시간 초과가 생겼다. 그리고 max 함수와 list를 썼을때도 시간 초과가 났다
# 그래서 max 함수 대신 직접 커스텀으로 최대값을 찾은 max_num 함수를 만들고, list를 사용하지 않았더니 통과가 됬다.
# 거의 3시간 풀었다... 답이 없다...
# 1
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a1 = format(arr1[i], 'b').zfill(n)
        a2 = format(arr2[i], 'b').zfill(n)
        s = ''
        for j in range(n):
            if a1[j] == '0' and a2[j] == '0':
                s += ' '
            else:
                s += '#'
        answer.append(s)
    return answer


# 2
def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        s = format(i|j, 'b').rjust(n, '0')
        s = s.replace('1', '#')
        s = s.replace('0', ' ')
        answer.append(s)
    return answer
# zfill(n) 대신 rjust(n, '0')을 활용해도 됨, just, rjust, ljust는 정렬 함수 rjust는 오른쪽으로 정렬
# 0이 아닌 다른 문자를 집어넣어야 할때 활용성이 클 것 같음

def reverse(u):
    result = ''
    for n in u:
        if n == '(':
            result += ')'
        else:
            result += '('
    return result

def remove_brk(n, u, v):
    global answer
    if n == '':
        return
    u_cnt = 0
    v_cnt = 0
    for i in n:
        if i =='(':
            u_cnt += 1
        else:
            v_cnt += 1
        if u_cnt == v_cnt:
            break
    idx = u_cnt + v_cnt
    u, v = n[:idx], n[idx:]
    if u[0] == '(':
        answer += u
        remove_brk(v, '', '')
    else:
        answer += '('
        remove_brk(v, '', '')
        answer += ')'
        u = u[1:-1]
        answer += reverse(u)
        
    

    
def solution(p):
    remove_brk(p, '', '')
    return answer

answer = ''

# 처음에 u = u[1:-1]로 맨앞과 뒤를 잘라낸 후, 뒤집을 때 그냥 u = u[::-1]로 문자열 자체를 거꾸로 했다.
# 그렇지만 예외가 있었다. "))()))((((" 이런 경우엔 v는 빈 문자열이고 u가 그 자체가 되는데 앞, 뒤를 잘라내도 대칭이 아니여서 뒤집기를 하게 되면 문제가 요구하는 변환을 할 수가 없다.
# 따라서 reverse 함수를 따로 만들어서 바꾸어 주어서 해결했다.
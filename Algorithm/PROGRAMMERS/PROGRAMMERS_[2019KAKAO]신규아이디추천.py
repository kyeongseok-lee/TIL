# 처음
def solution(a):
    ss = '-_.~!@#$%^&*()=+[{]}:?,<>/'
    ss = list(ss)
    ss.remove('.')
    ss.remove('-')
    ss.remove('_')
    a = a.lower()
    s = ''
    for i in a:
        if i not in ss:
            s += i
    a = s[0]
    for i in range(1, len(s)):
        if s[i] == '.' and s[i-1] == '.':
            continue
        a += s[i]
    if len(a) != 0:
        if a[0] == '.':
            a = a[1:]
    if len(a) != 0:       
        if a[-1] == '.':
            a = a[:-1]

    if a == '':
        a = 'a'
    if len(a) > 15:
        a = a[:15]

    while len(a) < 3:
        a += a[-1]
    
    if a[-1] == '.':
        a = a[:-1]
    return a


# 2 정리 
def solution(new_id):
    # lv1
    new_id = new_id.lower()
    
    # lv2
    answer = ''
    for s in new_id:
        if s.isalpha() or s.isdigit() or s in ['.', '-', '_']:
            answer += s
    
    # lv3
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    # lv4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else answer
    
    if answer[-1] == '.':
        answer = answer[:-1]

    # lv5
    if answer == '':
        answer = 'a'
    
    # lv6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # lv7
    while len(answer) < 3:
        answer += answer[-1]
    
    return answer
    

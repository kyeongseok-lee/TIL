def calculator(cal, a, b):
    if cal == '+':
        return a + b
    elif cal == '-':
        return a - b
    elif cal == '*':
        return a * b
    else:
        return a // b

for t in range(1, int(input()) + 1):
    info = list(input().split())
    
    result = 0
    stack = []
    cals = ['+', '-', '*', '/']
    for i in range(len(info)-1):
        if info[i] in cals:
            if len(stack) < 2:
                result = 'error'
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(calculator(info[i], a, b))
        else:
            stack.append(int(info[i]))

    if result == 0 and len(stack) == 1:
        result = stack[0]
    else:
        result = 'error'

    print('#%d' % t, result)
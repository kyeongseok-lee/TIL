def review_strings(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '{':
            stack.append(s[i])
        elif s[i] == ')':
            if len(stack) == 0:
                return 0
            elif stack[-1] == '(':
                stack.pop()
            else:
                return 0
        elif s[i] == '}':
            if len(stack) == 0:
                return 0
            elif stack[-1] == '{':
                stack.pop()
            else:
                return 0

    if len(stack) == 0:
        return 1
    else:
        return 0


for t in range(1, int(input()) + 1):
    strings = input()
    result = review_strings(strings)
    print('#%d' % t, result)    


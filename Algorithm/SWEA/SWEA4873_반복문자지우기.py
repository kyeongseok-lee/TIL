for t in range(1, int(input()) + 1):
    strings = input()
    
    stack = []
    for i in range(len(strings)):
        if len(stack) != 0 and stack[-1] == strings[i]:
            stack.pop()
        else:
            stack.append(strings[i])
    
    print('#%d' % t, len(stack))
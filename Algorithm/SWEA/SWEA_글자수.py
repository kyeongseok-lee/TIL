for t in range(1, int(input()) + 1):
    str1 = set(input())
    str2 = list(input())
    result = 0
    for s1 in str1:
        cnt = 0
        for s2 in str2:
            if s1 == s2:
                cnt += 1
        if result < cnt:
            result = cnt
        
    print('#%d' % t, result)

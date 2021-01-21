# 1
for t in range(1, int(input()) + 1):
    str1 = input()
    str2 = input()

    n1, n2 = len(str1), len(str2)
    result = 0
    for i in range(n2-n1+1):
        if str1 == str2[i:i+n1]:
            result = 1
            break
    print('#%d' % t, result)

    
# 2
for t in range(1, int(input())+1):
    str1 = input()
    str2 = input()

    ln1 = len(str1)
    ln2 = len(str2)

    i = 0
    j = 0
    result = 0
    while i < ln1 and j < ln2:

        if str1[i] != str2[j]:
            j = j - i
            i = -1
        i += 1
        j += 1
        if i == ln1:
            result = 1

    print('#{} {}'.format(t, result))
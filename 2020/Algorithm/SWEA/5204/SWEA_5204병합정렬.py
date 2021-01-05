def merge_sort(arr):

    if len(arr) == 1:
        return arr

    m = len(arr) // 2
    left = arr[:m]
    right = arr[m:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)


def merge(arr1,arr2):
    global cnt
    
    if arr1[-1] > arr2[-1]:
        cnt += 1
    
    result = list()
    i = j = 0
    while i < len(arr1) or j < len(arr2):
        if i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        elif i < len(arr1):
            result.append(arr1[i])
            i += 1
        elif j < len(arr2):
            result.append(arr2[j])
            j += 1

    return result


import sys
sys.stdin = open('5204.txt', 'r')

for t in range(1, int(input()) + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    
    final = merge_sort(nums)
    print('#%d' % t, final[N//2], cnt)

# 1
for t in range(1, int(input()) + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    
    minN = maxN = nums[0]

    for i in range(1, N):
        if nums[i] > maxN:
            maxN = nums[i]
        if nums[i] < minN:
            minN = nums[i]
    
    print('#%d' % t, maxN-minN)




# 2
for t in range(1, int(input()) + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    print('#%d' % t, max(nums)-min(nums))
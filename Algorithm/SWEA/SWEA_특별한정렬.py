# 1
def maxN(s):
    for i in range(n-1, s, -1):
        if nums[i] > nums[i-1]:
            nums[i], nums[i-1] = nums[i-1], nums[i]

def minN(s):
    for i in range(n-1, s, -1):
        if nums[i] < nums[i-1]:
            nums[i], nums[i-1] = nums[i-1], nums[i]

for t in range(1, int(input()) + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    n = len(nums)
    for k in range(n):
        if k % 2 == 0:
            maxN(k)
        else:
            minN(k)
    nums = nums[:10]
    print('#%d' % t, end=' ')
    for num in nums:
        print(num, end=' ')
    print()


# 2
for t in range(1, int(iuput()) + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    new_list = []
    nums.sort()
    k = -1
    a = 0
    for i in range(N//2):
        new_list.append(nums[k])
        new_list.append(nums[a])
        k -= 1
        a += 1
    new_list = new_list[:10]
           
    print('#%d' % t, end=' ')
    for k in new_list:
        print(k, end=' ')
    print()
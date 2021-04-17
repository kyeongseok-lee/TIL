from itertools import permutations
from collections import deque

def calculation(n1, n2, cal):
    if cal == '+':
        return n1 + n2
    elif cal == '-':
        return n1 - n2
    elif cal == '*':
        return n1 * n2
    else:
        if n1 < 0:
            return - (-n1 // n2)
        else:
            return n1 // n2

N = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

cal = ['+'] * plus + ['-'] * minus + ['*'] * mul + ['//'] * div 

permu = permutations(cal, len(cal))

cals = list(set(permu))

max_num = -1000000000
min_num = -max_num

for cal in cals:
    result = 0
    cal = deque(cal)
    num = deque(nums)
    while cal:
        n1 = num.popleft()
        n2 = num.popleft()
        cl = cal.popleft()

        num.appendleft(calculation(n1, n2, cl))


    max_num = max(max_num, num[0])
    min_num = min(min_num, num[0])  
    
print(max_num)
print(min_num)
    

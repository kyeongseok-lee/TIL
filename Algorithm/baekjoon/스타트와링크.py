from itertools import combinations, permutations
from collections import deque

def sum_s(slist, S):
    result = 0
    for s in slist:
        result += S[s[0]][s[1]]
    return result

N = int(input())
nums = [n for n in range(N)]
S = [list(map(int, input().split())) for _ in range(N)]

team = deque(combinations(nums, N//2))

balance = N * 100
while team:
    start = team.popleft()
    link = team.pop()

    start_perm = list(permutations(start, 2))
    link_perm = list(permutations(link, 2))

    balance = min(balance, abs(sum_s(start_perm, S)-sum_s(link_perm, S)))

print(balance)


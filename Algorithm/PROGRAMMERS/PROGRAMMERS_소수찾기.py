# 1 내 풀이
def makeNumbers(s, e, n, v, numbers, order, result):
    if s == e:
        num =  int("".join(order))
        if num not in result:
            result.append(num)
        return

    for i in range(n):
        if v[i]:
            continue
        v[i] = 1
        order.append(numbers[i])
        makeNumbers(s+1, e, n, v, numbers, order, result)
        v[i] = 0
        order.pop()
    
    


def findPrime(numbers):
    cnt = 0
    for num in numbers:
        if num < 2:
            continue
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                break
        else:
            cnt += 1
    return cnt


def solution(numbers):
    ln = len(numbers)
    result = []
    for i in range(1, ln+1):
        makeNumbers(0, i, ln, [0]*ln, numbers, [], result)

    return findPrime(result)

# 재귀로 순열을 구현하고, 소수 판별 함수로 소수의 개수를 반환 받았다.

# 2 다른사람 풀이
from itertools import permutations

def solution(numbers):
    result = set()
    for i in range(1, len(numbers)+1):
        result.update(set(map(int, map("".join, permutations(numbers, i)))))
        # result |= set(map(int, map("".join, permutations(numbers, i))))
    for i in range(2, int(max(result)**0.5) + 1):
        result -= set(range(i*2, max(result) + 1, i))
    result -= set(range(0, 2))
    return len(result)

# permutations를 사용한 순열로 숫자를 모으고  에라토스테네스의 체 알고리즘을 활용하여 소수를 찾는다.

# def prime_list(n):
#     # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
#     sieve = [True] * n

#     # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
#     m = int(n ** 0.5)
#     for i in range(2, m + 1):
#         if sieve[i] == True:           # i가 소수인 경우
#             for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
#                 sieve[j] = False

#     # 소수 목록 산출
#     return [i for i in range(2, n) if sieve[i] == True]

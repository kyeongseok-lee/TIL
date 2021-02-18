# 1
def solution(n, m):
    answer = []
    f1, f2 = 0, 0
    if n > m:
        for i in range(1, m+1):
            if n % i == 0 and m % i == 0:
                f1 = i
        for i in range(n, n*m+1):
            if i % n == 0 and i % m == 0:
                f2 = i
                break
    else:
        for i in range(1, n+1):
            if n % i == 0 and m % i == 0:
                f1 = i
        for i in range(m, n*m+1):
            if i % n == 0 and i % m == 0:
                f2 = i
                break
    answer.append(f1)
    answer.append(f2)
    
    return answer

# 2
def solution(n, m):
    num1, num2 = max(n, m), min(n, m)
    
    while num2:
        num1, num2 = num2, num1 % num2
    answer = [num1, n*m/num1]

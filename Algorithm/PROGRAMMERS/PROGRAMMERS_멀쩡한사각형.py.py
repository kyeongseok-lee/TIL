def solution(w, h):
    n = max_num(w, h)

    nw, nh = w // n, h // n

    useless = nw + nh - 1

    result = w * h - useless * n

    return result 


def max_num(w, h):
    e = min(w, h)
    result = 1
    for i in range(2, e+1):
        if w % i == 0 and h % i == 0:
            result = i 
    return result


# 최대 공약수는 math의 gcd를 사용해도 좋다
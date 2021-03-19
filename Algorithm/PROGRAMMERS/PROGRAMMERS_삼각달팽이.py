def solution(n):
    answer = []
    pyramid = [[0] * i for i in range(1, n+1)]
    num = 1
    r, c = -1, 0
    for rotate in range(n):
        for _ in range(n - rotate):
            if rotate % 3 == 0:
                r += 1
            elif rotate % 3 == 1:
                c += 1
            else:
                r -= 1
                c -= 1
            pyramid[r][c] = num
            num += 1

    answer = [number for row in pyramid for number in row]
    return answer

# 처음에 pyramid를 빈 리스트로 생성하여, 하나씩 집어넣는 방식으로 했다. 그러다 보니 뒤로 계속 숫자들을 넣기 때문에 숫자의 정렬이 제대로 되지 않았다.
# 따라서 각 칸마다 미리 0으로 정의해두고 각 행렬에 숫자를 넣어주는 방식으로 바꿨더니 간단해졌다. 거의 1시간 30분 이상 헤맸는데 방법을 바꾸고 바로 해결했다.
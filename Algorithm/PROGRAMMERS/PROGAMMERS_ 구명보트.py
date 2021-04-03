def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    l = 0
    r = len(people) - 1
    while l <= r:
        if people[l] + people[r] <= limit:
            l += 1
            r -= 1
            answer += 1
        else:
            l += 1
            answer += 1

    return answer

# 처음에는 pop을 활용하여 진행했는데, 효율성에서 0점이 나왔다.
# 그래서 인덱스로 접근해서 해결했다. 질문의 도움을 받았다.


# 2
from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    while people:
        if len(people) == 1:
            answer += 1
            break
        s = people.pop()
        if s + people[0] <= limit:
            people.popleft()
        answer += 1

    return answer

# 원래 풀려던 pop을 쓰려면, deque를 사용해야 효율성에서 런타임 에러가 나지 않는다.
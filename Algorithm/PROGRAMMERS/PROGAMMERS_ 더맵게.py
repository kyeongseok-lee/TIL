import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        if scoville[0] >= K:
            break
        new = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, new)
        answer += 1
    
    if len(scoville) == 0 or scoville[0] < K:
        return -1

    return answer


# 힙 자료구조를 이용하여 풀면 쉽게 풀린다.
# 최소 힙을 사용한 방식이다. 최소 힙내의 모든 원소 k는 항상 자식 노드인 (2k+1) (2K+2) 보다 크기가 같거나 작도록 원소가 추가된다.
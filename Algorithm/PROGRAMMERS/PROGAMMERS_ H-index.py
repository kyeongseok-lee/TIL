# 1 내풀이... 시간이 오래걸렸다..
def solution(citations):
    answer = 0
    citations.sort()
    cnt = [0] * (citations[-1] + 1)

    for i in range(len(citations)):
        for j in range(citations[i] + 1):
            cnt[j] += 1
    
    for i in range(len(cnt)):
        if i > cnt[i]:
            break
        if i <= cnt[i] and answer < i:
            answer = i
    return answer

print(solution([3, 0, 6, 1, 5]))



# 2 정렬을 거꾸로 해서 하면 위의 작업들이 필요없이
# 지금 인덱스에서의 값보다 인덱스가 같거나 작으면 인덱스 만큼의 숫자가 있다는 뜻이니 
def solution(citations):
  sorted_citations = sorted(citations, reverse=True)
  for i in range(len(sorted_citations)):
    if sorted_citations[i] <= i: 
      return i
  return len(sorted_citations)


# 3 원래 정렬대로 해도 방법이 있다.
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
    
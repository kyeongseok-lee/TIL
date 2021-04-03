def solution(num):
    num = list(map(str, num)) 
    num.sort(key = lambda x : x*3, reverse = True) 
    return str(int(''.join(num)))


print(solution([151, 15, 1]))


# 못풀엇다... 런타임 에러
# 별 생쇼을 다했다.. 핵심은 num의 숫자는 각각 1000보다 작다. 따라서 문자열로 바꾸고
# 각 문자의 * 3을 해서 모든 숫자들을 최소한 3자리까지 만들어 놓고 비교를 하면 된다.
# 문자열은 ASCI 값으로 비교를 하기 떄문에 첫번째 숫자로 비교를 한다.
# 이 개념만 알면 금방 푸는걸 너무 헤매고 결국 힌트를 얻어 풀었다..

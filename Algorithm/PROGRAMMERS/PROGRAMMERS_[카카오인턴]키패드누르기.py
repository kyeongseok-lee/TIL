def solution(numbers, hand):
    answer = ''
    lh = [1, 4, 7]
    rh = [3, 6, 9]
    mh = {2: [3, 1, 0, 1, 2, 1, 2, 3, 3, 3, 4],
          5: [2, 2, 1, 2, 1, 0, 1, 2, 1, 2, 3],
          8: [1, 3, 2, 3, 2, 1, 2, 1, 0, 1, 2],
          0: [0, 4, 3, 4, 3, 2, 3, 2, 1, 2, 1]
    }
    l, r = 10, 10
    
    for n in numbers:
        if n in lh:
            answer += 'L'
            l = n
        elif n in rh:
            answer += 'R'
            r = n
        else:
            ld = mh[n][l]
            rd = mh[n][r]
            if ld > rd:
                answer += 'R'
                r = n
            elif ld < rd:
                answer += 'L'
                l = n
            else:
                if hand == 'right':
                    answer += 'R'
                    r = n
                else:
                    answer += 'L'
                    l = n
    return answer

a = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
print(solution(a, 'left'))


# 모든 자판의 위치를 배열로 표현해서 활용하는 방법도 있다.
# phone_board = {
#             1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 
#             5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1),
#             9:(2,2), '*':(3,0), 0:(3,1), '#':(3,2)
# }
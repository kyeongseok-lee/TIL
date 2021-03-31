def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False

    return answer


# 효율성에서 생각을 잘해야 한다. 
# 정렬을 하게 되면 2개의 숫자만 비교하면 된다. 정렬을 하게 되면 11 121 11 이렇게 될 수가 없다. 따라서 앞뒤 두개만 비교를 해주면 된다.
# 이 개념이 없어서 효율성에서 계속 틀렸다..

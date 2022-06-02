# 내가 작성한 코드
# 정확성을 모두 통과했지만 마지막 효율성 테스트를 통과하지 못한 코드
# 리스트를 제거하여 N을 낮추는 방법으로 접근하려고 했지만 효율성을 통과하지 못한 코드

def solution(phone_book):
    while len(phone_book) != 1:
        before_i = phone_book[0]
        phone_book.remove(phone_book[0])
        l = len(phone_book[0])
        for j in phone_book:
            if before_i in j[:l]:
                return False
    return True

print(solution(["12","123","1235","567","88"]))

# 다른 사람이 작성한 코드
# N을 낮출 필요없이 sort를 통해 다음 인덱스만 확인해도 판별이 가능한 코드

def solution(phone_book):
    phone_book.sort()
    print(phone_book)
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True

# 다른 사람이 작성한 코드
# 문제 카테고리 hash 방식을 이용한 코드

def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                return False
    return answer
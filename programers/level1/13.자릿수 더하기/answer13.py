def solution(n):
    return sum([int(i) for i in str(n)])


def solution(number):
    if number < 10:
        return number
    return (number % 10) + solution(number // 10) 

print("결과 : {}".format(solution(123)))
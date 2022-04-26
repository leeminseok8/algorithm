def solution(a, b):
    answer = 0
    c = abs(a-b)
    for i in range(c+1):
        if a > b:
            answer += b+i
        elif b > a:
            answer += a+i
        else:
            return a
    return answer

print(solution(3, 5))
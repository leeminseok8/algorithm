def solution(n):
    re = ''
    while n >= 3:
        div_n = divmod(n, 3)
        re += str(div_n[1])
        if div_n[0]>=3:
            n = div_n[0]
        else:
            re += str(div_n[0])
            n = div_n[0]

    return int(re, 3)

print(solution(10))

# 다른 풀이
def solution(n):
    answer = ''
    while n > 0:
        answer += str(n%3)
        n = n//3
    answer = int(answer, 3)
    return answer

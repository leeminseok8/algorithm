import math

def solution(n):
    answer = ''
    a = '수박'*math.ceil(n/2)
    for i in range(n):
        answer += a[i]
    return answer

print(solution(8))

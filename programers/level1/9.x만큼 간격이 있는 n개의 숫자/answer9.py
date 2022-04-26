def solution(x, n):
    answer = []
    for i in range(n):
        x = x*(i+1)
        answer.append(x)
        x = x/(i+1)
    return answer

print(solution(6, 8))
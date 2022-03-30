def solution(s):
    p = s.split()
    answer = ""
    for i in range(len(p)):
        for j in range(len(p[i])):
            if j % 2 == 0:
                answer += p[i][j].upper()
            else:
                answer += p[i][j].lower()
        answer += ' '
    return answer[:-1]

print(solution("try split mission"))
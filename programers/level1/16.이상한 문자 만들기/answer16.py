def solution(s):
    p = s.split(" ")
    answer = ""
    for i in p:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += " "
    return answer[:-1]
    
print(solution("try split mission"))
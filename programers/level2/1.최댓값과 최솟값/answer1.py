def solution(s):
    array_s = list(map(int, s.split()))
    answer = str(min(array_s)) + " " + str(max(array_s))
    return answer

print(solution("1 4 3 2 5"))
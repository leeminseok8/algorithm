from operator import index


def solution(x):
    string = str(x)
    a = 0
    for i in range(len(string)):
        a += int(string[i])
    if x % a == 0:
        answer = True
    else:
        answer = False
    return answer

print(solution(1234))
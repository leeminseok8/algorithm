def solution(n):
    i = 2
    while n%i != 1:
        i += 1
    return i

print(solution(14022))
def solution(a, b):
    sum = 0
    for i in range(len(a)):
        sum += a[i]*b[i]
    return sum

print(solution([1,2,-1],[3,4,1]))
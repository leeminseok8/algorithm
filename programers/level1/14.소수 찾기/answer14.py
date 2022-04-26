def solution(n):
    count = 0
    i = 1
    a = 0
    while i <= n:
        for j in range(i):
            if i%(j+1) == 0:
                a += 1
        if a == 2:
            count += 1
        i += 1
        a = 0
    return count

print(solution(10))
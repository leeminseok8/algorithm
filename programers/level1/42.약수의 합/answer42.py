def solution(n):
    d = 1
    sum_d = 0
    while d <= n:
        if n%d == 0:
            sum_d += d
        d += 1
    return sum_d

print(solution(20))

#return n + sum(i for i in range(1, int(n**.5) + 1) if n % i == 0)
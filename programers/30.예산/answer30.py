def solution(d, budget):
    s = sorted(d)
    for i in range(len(s)):
        if sum(s[:i+1]) > budget:
            return i
    return len(s)

print(solution([1,1,1], 2))
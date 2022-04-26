def solution(arr, divisor):
    a = []
    for i in arr:
        if i % divisor == 0:
            a.append(i)
    if len(a) == 0:
        return [-1]
    return sorted(a)

# def solution(arr, divisor):
#     return sorted([n for n in arr if n%divisor == 0]) or [-1]

print(solution([1, 2, 3, 10, 14, 20, 30], 5))
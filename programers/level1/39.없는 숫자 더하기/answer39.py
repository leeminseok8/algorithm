def solution(numbers):
    num_range = [1,2,3,4,5,6,7,8,9]
    for i in numbers:
        if i in num_range:
            num_range.remove(i)
    return sum(num_range)

# def solution(numbers):
#     return 45 - sum(numbers)

print(solution([1,2,3,4,5]))
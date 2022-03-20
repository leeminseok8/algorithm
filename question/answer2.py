def solution(arr):
    answer = 0
    a = 0
    for i in range(len(arr)):
        a += arr[i]
        answer = a / len(arr)
    return answer

print(solution([1, 2, 3]))

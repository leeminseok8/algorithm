def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i < j:
                if not numbers[i]+numbers[j] in answer:
                    answer.append(numbers[i]+numbers[j])

    return sorted(answer)
    
print(solution([2,2,3,4,6,7,8,9]))
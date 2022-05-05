def solution(arr1, arr2):
    answer_arr = []
    for i, j in zip(arr1, arr2):
        sum_arr = []
        for x, y in zip(i, j):
            sum_arr.append(x+y)
        answer_arr.append(sum_arr)

    return answer_arr

print(solution([[1,2],[2,3]],[[3,4],[4,5]]))
def solution(answers):
    per_1 = [1,2,3,4,5]
    per_2 = [2,1,2,3,2,4,2,5]
    per_3 = [3,3,1,1,2,2,4,4,5,5]
    count_1 = 0
    count_2 = 0
    count_3 = 0
    max_per = []
    for i in range(len(answers)):
        if answers[i] == per_1[i%5]:
            count_1 += 1
        if answers[i] == per_2[i%8]:
            count_2 += 1
        if answers[i] == per_3[i%10]:
            count_3 += 1

    if max(count_1, count_2, count_3) == count_1:
        max_per.append(1)
    if max(count_1, count_2, count_3) == count_2:
        max_per.append(2)
    if max(count_1, count_2, count_3) == count_3:
        max_per.append(3)
    
    return max_per

print(solution([1,3,2,4,2]))
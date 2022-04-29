def solution(n, lost, reserve):
    i = 1
    dic_n = {}
    while i <= n :
        if i not in dic_n:
            dic_n[i] = 1

            if i in lost and i not in reserve:
                dic_n[i] -= 1
            elif i in reserve and i not in lost:
                dic_n[i] += 1
        i += 1
    
    for j in range(n):
        if dic_n[j+1] == 2:
            if j != 0 and dic_n[j] == 0:
                dic_n[j+1] -= 1
                dic_n[j] += 1
            elif j+2 <= n and dic_n[j+2] == 0:
                dic_n[j+1] -= 1
                dic_n[j+2] += 1

    return len([n for n in dic_n.keys() if dic_n[n]>=1])

print(solution(6, [1,3,5], [2,4,6]))
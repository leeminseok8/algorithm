def solution(array, commands):
    div_arr = []
    for i in commands:
        div_arr.append(sorted(array[i[0]-1:i[1]])[i[2]-1])
    return div_arr

# return [sorted(array[a-1:b])[c-1] for a,b,c in commands]

print(solution([1,2,3,4,5,6], [[1,3,1],[2,4,2],[1,5,3]]))
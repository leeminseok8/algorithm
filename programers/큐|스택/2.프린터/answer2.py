def solution(priorities, location):
    array1 = [c for c in range(len(priorities))]
    array2 = priorities.copy()

    i = 0
    while True:
        if array2[i] < max(array2[i+1:]):
            array1.append(array1.pop(i))
            array2.append(array2.pop(i))
        else:
            i += 1

        if array2 == sorted(array2, reverse=True):
            break

    return array1.index(location) + 1

print(solution([1, 1, 9, 1, 1, 1], 0))
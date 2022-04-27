def solution(nums):
    dic_pok = {}
    for i in nums:
        if i not in dic_pok:
            dic_pok[i] = 1
        else:
            dic_pok[i] += 1
    if len(dic_pok.keys()) >= len(nums)/2:
        return len(nums)/2
    elif len(dic_pok.keys()) < len(nums)/2:
        return len(dic_pok.keys())

print(solution([1,2,2,1,3,4]))
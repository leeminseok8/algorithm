def solution(participant, completion):
    # for i in participant:
    #     if i not in completion:
    #         return i
    #     elif participant.count(i) > completion.count(i):
    #         return i

    # n = 0
    # while len(participant) != 1:
    #     par = participant[n]
    #     if par not in completion:
    #         return par
    #     elif participant.count(par) > completion.count(par):
    #         return par
    #     n += 1

    p_dict = {}
    for p in participant:
        if p not in p_dict:
            p_dict[p] = 1
        else:
            p_dict[p] += 1
            
    for c in completion:
        p_dict[c] -= 1

    result = [key for key, value in p_dict.items() if value > 0]
    answer = result[0]

    return answer

print(solution(['a','e','b','d'],['a','b','d']))
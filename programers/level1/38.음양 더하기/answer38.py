def solution(absolutes, signs):
    result = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            result += absolutes[i]
        elif signs[i] == False:
            result += -absolutes[i]
    return result

print(solution([1,3,4,10,2],[True,True,True,False,False]))

# def solution(absolutes, signs):
#     answer=0
#     for absolute,sign in zip(absolutes,signs):
#         if sign:
#             answer+=absolute
#         else:
#             answer-=absolute
#     return answer
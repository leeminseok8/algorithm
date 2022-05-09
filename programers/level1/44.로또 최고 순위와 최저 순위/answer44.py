def solution(lottos, win_nums):
    result = []
    rewords = []
    rewords_0 = 0
    for i in lottos:
        if i in win_nums:
            rewords.append(i)
        elif i == 0:
            rewords_0 += 1
            
    result.append(len(lottos)-len(rewords)-rewords_0+1)
    result.append(len(lottos)-len(rewords)+1)
    
    if len(rewords) < 2:
        result[1] = 6
    if len(rewords) == 0 and rewords_0 == 0:
        result[0] = 6
    return result

print(solution(	[44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))

# def solution(lottos, win_nums):

#     rank=[6,6,5,4,3,2,1]

#     cnt_0 = lottos.count(0)
#     ans = 0
#     for x in win_nums:
#         if x in lottos:
#             ans += 1
#     return rank[cnt_0 + ans],rank[ans]
def solution(id_list, report, k):
    fired_list = {}
    pattern_list = {}
    for fire in report:
        pattern_list[fire] = 1
        fire = fire.split(' ')
        if fire[1] not in fired_list and fire[0]+' '+fire[1] not in pattern_list:
            fired_list[fire[1]] = 1
        elif fire[1] in fired_list and fire[0]+' '+fire[1] not in pattern_list:
            fired_list[fire[1]] += 1
        
    return fired_list

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]))

# a = {'abc' : 'def', 'def' : 'hij'}
# a['abc'] = 'aaa'
# b = 'abc def'
# b = b.split(' ')
# print(b[0]+' '+b[1])


# 누가 누구 신고?
# 신고당한 횟수
# 정지된 아이디
# 신고자와 피신고자의 관계 1:N
# 중복시 1회 인정
# 내가 누구를 몇 회 신고한 지 / 내가 신고당한 횟수를 인지해야 함
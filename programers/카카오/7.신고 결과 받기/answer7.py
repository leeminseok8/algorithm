# def solution(id_list, report, k):
#     # 신고 받은 사람과 횟수
#     fired_list = {}
#     # 신고자와 피신고자 중복 확인
#     pattern_list = {}
#     for fire in report:
#         fire = fire.split(' ')
#         if fire[1] not in fired_list and fire[0]+' '+fire[1] not in pattern_list:
#             pattern_list[fire[0]+' '+fire[1]] = 1
#             fired_list[fire[1]] = 1
#         elif fire[1] in fired_list and fire[0]+' '+fire[1] not in pattern_list:
#             fired_list[fire[1]] += 1
        
#     return fired_list

from collections import defaultdict

def solution(id_list, report, k):
    count_d = defaultdict(int)
    report_d = defaultdict(set)
    answer = [0 for _ in range(len(id_list))]

    # 신고내역 (set 사용으로 중복 제외)
    for x in report:
        person, reported = x.split()
        report_d[person].add(reported)

    # ID 별 신고 카운트
    for x in report_d.values():
        for y in x:
            count_d[y] += 1

    # 신고 받은 사람들의 신고 카운트를 센 뒤 answer에 저장
    for idx, x in enumerate(id_list):
        for y in report_d[x]:
            if count_d[y] >= k:
                answer[idx] += 1

    return answer


def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], k=2))
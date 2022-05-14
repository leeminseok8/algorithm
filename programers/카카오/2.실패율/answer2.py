def solution(N, stages):
    count_stage = {}
    total_person = 0
    fail_rate = {}
    answer = []

    for i in range(N):
        count_stage[i+1] = stages.count(i+1)

    for i in range(N):
        total_person += stages.count(i)
        if count_stage[i+1] != 0:
            fail_rate[i+1] = count_stage[i+1] / (len(stages)-total_person)
        else:
            fail_rate[i+1] = 0

    a = sorted(fail_rate.items(), key=lambda x: x[1], reverse=True)
    
    for i in a:
        answer.append(i[0])
    
    return answer

print(solution(5,[2,1,2,6,2,4,3,3]))    # [3,4,2,1,5]

def solution(N, stages):
    answer = []
    fail = []
    info = [0] * (N + 2)
    for stage in stages:
        info[stage] += 1
    for i in range(N):
        be = sum(info[(i + 1):])
        yet = info[i + 1]
        if be == 0:
            fail.append((i + 1, 0))
        else:
            fail.append((i + 1, yet / be))
    for item in sorted(fail, key=lambda x: x[1], reverse=True):
        answer.append(item[0])
    return answer
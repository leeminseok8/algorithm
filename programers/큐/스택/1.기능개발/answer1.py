import math

# 내가 작성한 코드

def solution(progresses, speeds):
    re_progress = [100] * len(progresses)
    days = []
    
    for i in range(len(progresses)):
        progress = re_progress[i] - progresses[i]
        days.append(math.ceil(progress / speeds[i]))
    
    diff = [days[0]]
    result = [1]

    for i in range(len(days)-1):
        if diff[0] < days[i+1]:
            result.append(1)
            diff[0] = days[i+1]
        else: 
            result[-1] = result[-1] + 1
    return result

print(solution([96, 99, 98, 97], [1, 1, 1, 1]))

# 다른 사람이 작성한 코드
# zip을 통해 수식을 함축하여 코드의 길이를 최소화한 코드인 것 같다.

def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]

# 다른 사람이 작성한 코드
# 조건들을 모두 변수화하여 알아보기 쉬운 코드인 것 같다.
# 다른 풀이 중에 가장 알고리즘 풀이에 적합한 방법이 아닐까.

def solution(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
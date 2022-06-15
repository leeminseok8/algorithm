# 내가 작성한 코드
# 알고리즘은 다른 방식과 유사하지만 중복되는 함수로 시간복잡도를 줄이지 못했다.

def solution(people, limit):
    people = sorted(people, reverse=True)
    boat = []
    cnt = 0
    i = 0
    
    while len(people) != 0:
        if len(boat) == 0:
            boat.append(people[-1])
            people.pop()
        if len(people) == 0:
            return cnt + 1
        elif boat[0] + people[i] <= limit:
            boat.pop()
            people.pop(i)
            cnt += 1
            i = 0
            continue
        if i < len(people)-1:
            i += 1
        else:
            boat.pop()
            cnt += 1
            i = 0
    return cnt

print(solution([70, 50, 80, 50], 100))

# 다른 사람이 작성한 코드
# deque를 이용하여 시간복잡도를 줄인 코드

from collections import deque
def solution(people, limit):
    answer = 0
    deq = deque(sorted(people))
    while deq:
        if len(deq) == 1:
            answer += 1
            break
        if deq[0] + deq[-1] <= limit:
            deq.pop()
            deq.popleft()
        else:
            deq.pop()
        answer += 1
    return answer

# 다른 사람이 작성한 코드
# 같은 문제를 풀었지만 시간복잡되를 최소화 한 방식
# len(people) - answer를 사용한 아이디어가 인상깊다.

def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer
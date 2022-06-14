# 내가 작성한 코드
# 앞에서 부터 k값만큼 자리수를 만드므로 조합을 사용
# 100만자리까지 구하므로 시간 초과

from itertools import combinations

def solution(number, k):
    num = []
    array_num = [a for a in number]
    combi_num = list(combinations(array_num, len(array_num)-k))
    
    for i in combi_num:
        num.append("".join(i))
    return max(num)

# 다른 사람이 작성한 코드
# LIFO 스택 방식을 사용

def solution(number, k):
    answer = [] # Stack
    
    for num in number:
        if not answer:
            answer.append(num)
            continue
        if k > 0:
            while answer[-1] < num:
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
        answer.append(num)
        
    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)

print(solution("1924", 2))
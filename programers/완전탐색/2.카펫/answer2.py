# return의 인덱스 0,1에서 -2 씩 하고 *2 하고 +4해서 더했을 때 brown이 되어야 한다.
# return의 인덱스는 약수구하고 brown + yellw 값을 나누어 0,1을 구한다.

def solution(brown, yellow):
    sum_color = brown + yellow
    row = 0
    column = 0
    result_sum = 0
    answer = []
    i = 1
    
    while i <= int(sum_color**0.5):
        if sum_color%i == 0:
            row = i
            column = int(sum_color/i)
            result_sum = (row-2)*2 + (column-2)*2 + 4
            if brown == result_sum and column >= row:
                answer.append(column)
                answer.append(row)
                return answer
        i += 1

print(solution(10,2))

# 다른 사람이 작성한 코드
# 내가 작성한 코드를 최소화하면 아래의 코드 작성 가능
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]
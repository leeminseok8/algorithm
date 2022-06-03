# 내가 작성한 코드
# (의상종류 별 의상 수 + 1)씩 모두 곱하는 이유는 의상종류 별 의상수에 그 의상을 안 입는 경우의 수도 곱하는 것이다.
# 추가적으로 -1을 하는 이유는 아무것도 모두 안 입는 경우의 수를 빼는 것이다.

from functools import reduce

def solution(clothes):
    cloth_type = {}
    for cloth in clothes:
        if cloth[1] not in cloth_type:
            cloth_type[cloth[1]] = 1
        else:
            cloth_type[cloth[1]] += 1
    answer = reduce(lambda x,y : x*(y+1), cloth_type.values(), 1) - 1
    return answer

# 다른 사람이 작성한 코드
# Counter를 이용하면 굳이 dict를 만들지 않아도 key값을 카운트할 수 있다.
# reduce 함수를 보면 선택적으로 initializer 를 넘길 수가 있는데, 안넘기면 lambda를 최초로 계산할 때 x에 iterable[0]이 들어간다.

from collections import Counter
from functools import reduce

def solution(clothes):
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer

# 다른 사람이 작성한 코드
# 문제 카테고리인 hash에 가장 적합한 코드
# 외부 함수를 import하지 않아도 수학 공식만 알고 있다면 가능한 풀이 방법

def solution(clothes):
    clothes_type = {}

    for _, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1
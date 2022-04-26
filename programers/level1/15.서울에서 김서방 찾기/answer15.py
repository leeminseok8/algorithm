def solution(seoul):
    s = 0
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            s = i
    answer = f"김서방은 {s}에 있다"
    return answer



# def findKim(seoul):
#     return "김서방은 {}에 있다".format(seoul.index('Kim'))

print(solution(["Queen", "Tod", "Kim"]))
def solution(n):
    a = n**(1/2)
    s = str(a)
    if s[-2:] == '.0':
        a = float(s)
        a = int(a)
        answer = (a+1)**2
    else:
        answer = -1
    return answer
    
print(solution(144))
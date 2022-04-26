def solution(a, b):
    m = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    y = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    if a <= 1:
        return y[b%7]
    
    else:
        d = (sum(i for i in m[0:a-1]) + b) % 7
        return y[d]
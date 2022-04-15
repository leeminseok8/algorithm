def solution(a, b):
    m = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    y = ['SAT', 'SUN','MON','TUE','WED','THU','FRI']
    d = sum(i for i in m[0:a])
    p = (d + b)%7
    
    return y[p]
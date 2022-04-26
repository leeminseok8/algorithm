def solution(s):
    a = 0
    b = 0
    for i in s:
        if i == 'p' or i == 'P':
            a += 1
        elif i == 'y' or i == 'Y':
            b += 1
    if a == b:
        return True
    else:
        return False
    
print(solution('pdyfyq'))

    # def numPY(s):
        
    # return s.lower().count('p') == s.lower().count('y')
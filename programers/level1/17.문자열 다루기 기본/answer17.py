def solution(s):
    if len(s) == 4 or len(s) == 6:
        for i in list(s):
            if ord(i) <= 57:
                answer = True
            else:
                answer = False
                return answer
    else:
        answer = False
        return answer
    return answer

def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)
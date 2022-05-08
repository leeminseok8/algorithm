import string

def solution(s, n):
    change_s = ''
    for i in s:
        if i == ' ':
            change_s += i
        elif i in string.ascii_lowercase:
            a = ord(i) + n
            if a > 122:
                a -= 26
            change_s += chr(a)
        elif i in string.ascii_uppercase:
            a = ord(i) + n
            if a > 90:
                a -= 26
            change_s += chr(a)
    return change_s
    
print(solution('abc', 2))
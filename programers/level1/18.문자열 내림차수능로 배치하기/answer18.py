def solution(s):
    answer = ""
    re = []
    b = 0
    c = ""
    for i in s:
        b = ord(i)
        re.append(b)
    re.sort(reverse=True)
    for j in re:
        c = chr(j)
        answer += c
    return answer


def solution(s):
    return ''.join(sorted(s, reverse=True))
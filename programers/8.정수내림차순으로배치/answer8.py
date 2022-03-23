def solution(n):
    # l = [int(a) for a in str(n)]
    # l.sort(reverse=True)
    # s = [str(a) for a in l]
    # b = ''
    # for i in range(len(s)):
    #     b += s[i]
    # answer = int(b)
    # return answer
    
    ls = list(str(int(n)))
    ls.sort(reverse=True)
    return int("".join(ls))

print(solution(12345))
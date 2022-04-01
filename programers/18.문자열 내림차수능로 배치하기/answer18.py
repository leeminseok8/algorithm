def solution(s):
    # answer = ''
    a = []
    b = 0
    for i in s:
        b = ord(i)
        a.append(b)

    return a.sort()

# b = 'adf'
# c = b[1]

# print(c)
print(solution('abcde'))
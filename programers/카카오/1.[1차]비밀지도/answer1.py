def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        hint = ''
        a = str(bin(arr1[i]))[2:]
        b = str(bin(arr2[i]))[2:]
        if len(a) < n or len(b) < n:
            a = '0'*(n-len(a)) + a
            b = '0'*(n-len(b)) + b
        for x,y in zip(a,b):
            if x == '1' or y == '1':
                hint += '#'
            elif x == '0' and y == '0':
                hint += ' '
        answer.append(hint)
    return answer
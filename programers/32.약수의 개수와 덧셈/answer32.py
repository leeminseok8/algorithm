def solution(left, right):
    even = 0
    odd = 0
    for i in range(right-left+1):
        count = 0
        for j in range(1, int(left**(1/2))+1):
            if left%j == 0:
                count += 1
                if j**2 != left:
                    count += 1
        if count%2 == 0:
            even += left
        else:
            odd += left
        left += 1
        
    return abs(even-odd)

# 다른 사람 풀이
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer

print(solution(13, 17))
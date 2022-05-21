def solution(n):
    num = ''
    for i in range(n):
        num += str(i)

    return int(num[n])

print(solution(15))

# n의 범위가 1 <= n <= 100,000,000 이기 때문에 당연히 이렇게 할 경우 런타임에러 또는 효율성에 문제가 발생한다.
# 그러므로 어떤 자리수인지 특정하여 앞의 숫자들은 제하고 단위 내에서 탐색하는 알고리즘을 구상하자.

def solution(n):
    num = 0
    i = 1

    while num < n:    
        num += 10**i - 10**(i-1)
        if num > n:
            num -= 10**i - 10**(i-1)
            break
        i += 1

    a, b = divmod((n - num),i)
    result = int(str(10**(i-1) + a)[b])

    return result

print(solution(100000000))

# 기존이 코드는 input으로 1억을 넣으면 1억번의 for문을 동작해야 하지만,
# 아래와 같은 코드를 작성하면 9번의 동작으로 결과값이 반환된다.
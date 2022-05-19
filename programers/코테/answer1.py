def solution(n):
    num = ''
    for i in range(n):
        num += str(i)

    return int(num[n])

print(solution(15))

# n의 범위가 1 <= n <= 100,000,000 이기 때문에 당연히 이렇게 할 경우 런타임에러 또는 효율성에 문제가 발생한다.
# 그러므로 어떤 자리수인지 특정하여 앞의 숫자들은 제하고 단위 내에서 탐색하는 알고리즘을 구상하자.
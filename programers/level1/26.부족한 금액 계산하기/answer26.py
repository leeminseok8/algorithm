def solution(price, money, count):
    amount = 0
    for i in range(count):
        amount += price*(i+1)
    if money-amount >=0:
        return 0
    return abs(amount-money)

print(solution(100, 2000, 5))
# from datetime import datetime, timedelta

# departure_date = "2022-10-12"
# year, month, day = map(int,departure_date.split("-"))
# aware_datetime = datetime(year, month, day)
# time = aware_datetime+timedelta(seconds=6)
# print(time)

def solution(d, budget):
    s = sorted(d)
    for i in range(len(s)):
        if sum(s[:i+1]) > budget:
            return i
    return len(s)

print(solution([1,1,1], 2))

# s = [1,2,4,3,1]
# i = 2
# print(sum(s[:i]))
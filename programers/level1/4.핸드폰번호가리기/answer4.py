def solution(phone_number):
    l = len(phone_number)-4
    answer = l*'*'+phone_number[-4:]
    return answer

print(solution('01034348989'))
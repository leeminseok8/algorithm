from itertools import combinations

def solution(nums):
    nums_list = list(combinations(nums, 3))
    prime_number = 0

    for i in nums_list:
        count = 0
        for j in range(2,sum(i)):
            if (sum(i)%j) == 0:
                count += 1
        if count == 0:
            prime_number += 1
    return prime_number

###################################

from itertools import combinations

def is_prime_number(num):
    if num == 0 or num == 1:
        return False
    else:
        for n in range(2, (num//2)+1):
            if num%n == 0:
                return False
        
        return True

def solution(nums):
    answer = 0
    cmb = list(combinations(nums,3))
    for arr in cmb:
        if is_prime_number(sum(arr)):
            answer += 1
    
    return answer

print(solution([1,2,3,4,]))
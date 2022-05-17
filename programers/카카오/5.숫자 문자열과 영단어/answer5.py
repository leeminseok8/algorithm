def solution(s):
    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9

    if 'zero' in s:
        s = s.replace('zero', str(zero))

    if 'one' in s:
        s = s.replace('one', str(one))

    if 'two' in s:
        s = s.replace('two', str(two))

    if 'three' in s:
        s = s.replace('three', str(three))

    if 'four' in s:
        s = s.replace('four', str(four))

    if 'five' in s:
        s = s.replace('five', str(five))

    if 'six' in s:
        s = s.replace('six', str(six))

    if 'seven' in s:
        s = s.replace('seven', str(seven))

    if 'eight' in s:
        s = s.replace('eight', str(eight))

    if 'nine' in s:
        s = s.replace('nine', str(nine))

    return s

print(solution("one4seveneight"))

num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
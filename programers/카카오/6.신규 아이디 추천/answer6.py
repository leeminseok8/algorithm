import string

def solution(new_id):
    new_array = []
    new_str = ''

    new_id = new_id.lower()

    symbols = string.punctuation.replace('-', '').replace('_', '').replace('.', '')
    for symbol in symbols:
        new_id = new_id.replace(symbol, '')

    for id in range(len(new_id)):
        new_array.append(new_id[id])

        if new_id[id] == '.' and new_id[id] == new_id[id-1]:
            new_array.pop()
    
    for i in new_array:
        new_str += i
    
    new_str = new_str.strip('.')

    if new_str == '':
        new_str += 'a'

    if len(new_str) >= 16:
        new_str = new_str[:15].rstrip('.')

    while len(new_str) <= 2:
        new_str += new_str[-1]

    return new_str

print(solution("...!@BaT#*..y.abcdefghijklm")) # "bat.y.abcdefghi"

import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
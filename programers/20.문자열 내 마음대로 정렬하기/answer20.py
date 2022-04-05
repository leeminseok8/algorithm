def solution(strings, n):
    return sorted(sorted(strings), key=lambda x: x[n])

# a = [1, 2, 3, 6, 8, 7, 5]
# c = ['adf', 'bab', 'def', 'edd', 'cqd']
# b = sorted(c, key=lambda x: x[1])
# print(b)
# strings = ['daac', 'cba', 'babb', 'ecad']
# d = sorted(strings)
# e = sorted(d, key=lambda x: x[1])
# print(e)

# f = 'a', 'b', 'c'
# list(f)
# print(f)

# g = list(map(str, a))
# print(g)
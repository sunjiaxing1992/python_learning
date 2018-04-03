names = ['sun', 'jia', 'xing']
for name in names:
    print(name)

# sun
# jia
# xing

another_names = ['s', 'j', 'x']
for name in another_names:
    print(name + " is a good student")

# s is a good student
# j is a good student
# x is a good student




for num in range(1,5):
    print(num)

# 1
# 2
# 3
# 4

numbers = list(range(1, 6))
print(numbers)
# [1, 2, 3, 4, 5]

numberss = list(range(1, 6, 2))
print(numberss)
# [1, 3, 5]

squares = []
for value in range(1, 10, 2):
    square = value * value
    squares.append(square)
print(squares)
# [1, 9, 25, 49, 81]


nums = [1, 2, 3]
print(min(nums))
print(max(nums))
print(sum(nums))
# 1
# 3
# 6

sq = [v*v for v in range(1,8,3)]
print(sq)
# [1, 16, 49]       列表解析

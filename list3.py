nums = [1, 2, 3, 4, 5]
print(nums[0:2])
# [1, 2]

print(nums[:2])
print(nums[2:])
print(nums[-3:])
# [1, 2]
# [3, 4, 5]
# [3, 4, 5]

for v in nums[2:]:
    print(v)
# 3
# 4
# 5

my_nums = [1, 2, 3]
you_nums = my_nums[:]
my_nums.append(4)
print(my_nums)
print(you_nums)
# [1, 2, 3, 4]
# [1, 2, 3]

my = [1, 2]
you = my
my.append(3)
print(my)
print(you)
# [1, 2, 3]
# [1, 2, 3]


# 元祖 ： 不能修改的列表
num = (1, 2, 3)

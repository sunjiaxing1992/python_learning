lists = ['sun', 'jia', 'xing']
print(lists[1].title())

# Jia

print(lists[-1].title())

# Xing

lists.append('SUN')
print(lists)

# ['sun', 'jia', 'xing', 'SUN']

lists.insert(1, 'insert')
print(lists)

# ['sun', 'insert', 'jia', 'xing', 'SUN']

del lists[0]
print(lists)

#  ['insert', 'jia', 'xing', 'SUN']

ppop = lists.pop()
print(lists)
print(ppop)

# ['insert', 'jia', 'xing']
# SUN



another_list = [1, 2, 3, 4]
another_list.pop(2)
print(another_list)

# [1, 2, 4]


another_list.remove(2)
print(another_list)

# [1, 4]

mun_list = [4,3,5,2,9]
mun_list.sort()
print(mun_list)

mun_list.sort(reverse = True)
print(mun_list)

# [2, 3, 4, 5, 9]
# [9, 5, 4, 3, 2]


another_mun_list = [2, 3, 1, 6]
print(another_mun_list)
print(sorted(another_mun_list))
print(another_mun_list)

# [2, 3, 1, 6]
# [1, 2, 3, 6]
# [2, 3, 1, 6]


mu_list = [1, 3, 2]
mu_list.reverse()
print(mu_list)
print(len(mu_list))

# [2, 3, 1]
# 3
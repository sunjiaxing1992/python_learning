names = ('sun', 'jia', 'xing')
for name in names:
    if name == 'jia':
        print(name.title())
    else:
        print(name.upper())
# SUN
# Jia
# XING

a = 5
if a > 2 and a < 8:
    print(a)
if a < 9 or a > 12:
    print(a)

# 5
# 5


name = ['s', 'j', 'x']
if 'j' in name:
    print(True)
if "z" not in name:
    print(True)
# True
# True

age = 12
if age < 4:
    print("age < 4")
elif age < 16:
    print('age < 16')
else:
    print('age > 16')
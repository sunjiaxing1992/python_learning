people = { "age": 13, "name" : 'sun'}
print(people['age'])
print(people['name'])
# 13
# sun

people['class'] = '二年级'
print(people)
# {'age': 13, 'name': 'sun', 'class': '二年级'}

del people["age"]
print(people)
# {'name': 'sun', 'class': '二年级'}

name = {
    'f': 'sun',
    'm': 'jia',
    'l': 'xing'
}
for k,v in name.items():
    print(k)
    print(v)
# f
# sun
# m
# jia
# l
# xing

for k in name.keys():
    print(k)
for v in name.values():
    print(v)
# f
# m
# l
# sun
# jia
# xing

for k in sorted(name.keys()):
    print(k)
# f
# l
# m


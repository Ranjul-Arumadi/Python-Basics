'''
store in key -value pairs
- changable
- ordered
- no duplicates
'''

dic = {'name': 'Sam', 'age':23}
print(dic)
print(dic.get('name'))

print(dic.keys())
print(dic.values())
print(dic.items())

# traverse
for key in dic:
    print(key, dic[key])
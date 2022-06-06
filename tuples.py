'''
Tuples:

- unchangable [ we cannot change, add or remove items after the tuple has been created.]
- ordered
- duplicates is ok
'''

# workaround for unchangability
'''
1. read as tuple
2. make list and update
3. make tuple again
'''

a=(1,2,3)
a = list(a) #make as list
a.insert(1, 999)
a = tuple(a)
print(a)
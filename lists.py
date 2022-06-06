'''
List:

- Multiple values in a single variale
- ordered (adding new thing will go to end od list)
- changable (chnage, addd, remove items after creation)
- allow duplicates ()

- can have different data type values in a single list

'''

# append [extend wors the same way]
a = []
a.append(1)
a.append(2)

print(a)

# insert(position, value)

pos = 1
value = 999
a.insert(pos,value)
print(a)

#remove
a.remove(999)
print(a)

#pop  -remove last value
a.pop()
print(a)

#reverse
'''
a[::-1] -> does not modify the original list
a.reverse() -> modifies the list
'''

a.reverse()
print(a)

# concatenate

'''
The concatenate operation is used to merge two lists 
and return a single list. The + sign is used to perform 
the concatenation. Note that the individual lists are not
 modified, and a new combined list is returned
'''

#index

print(a.index(1)) #-> return index value where 1 is present

# simple search can be done using the 'in' operator


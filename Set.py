'''
sets are exactly like lists except for the fact
that their elements are immutable (that means you
cannot change/mutate an element of a set once declared). However,
you can add/remove elements from the set.
'''

a = set((1,2,3))
print(a)

a.update((999,))
print(a)

a.remove(1)
print(a)

'''
Operations:

- union |
- intersection &
- difference -
symmetric_difference ^
'''
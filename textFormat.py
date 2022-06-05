'''
1. center(): centre aligns the text
'''
txt = "ranjul"
print(txt.center(20, '*')) #'*' is optional, default is ' '

'''
2. capitalize(): Upper case the first letter in this sentence
'''
txt = 'helo, there'
print(txt.capitalize())

'''
3. casefold(): method returns a string where all the characters are lower case.

This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, 
meaning that it will convert more characters into lower case, and will find more matches when comparing 
two strings and both are converted using the casefold() method.
'''

a = 'HELO tHere HoW aRE yu'
print(a.casefold())
print(a.lower())

'''
4. count() method returns the number of times a specified value appears in the string.
'''

a = 'hello there lol'
print(a.count('l'))

'''
5. encode
'''
txt = "My name is Ståle"
print(txt.encode(encoding="ascii",errors="backslashreplace"))

'''
6. endswith() method returns True if the string ends with the specified value, otherwise False.
'''

a = 'hello there'
print(a.endswith('there'))
print(a.endswith('hello'))

'''
7. find(): Searches the string for a specified value and returns the position of where it was found
'''

a = 'hello ram'
print(a.find('ram'))

'''
8. placeholders
'''
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)

'''
9. 
'''
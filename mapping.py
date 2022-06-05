'''
This comes under higher order function:
they are functions that expect a function as a
argument.

Use:
Do same action to many values such as list item

'''

words = ["1", "2" , "3"]
map(int, words)

#this below line is important as change will be
#only reflected if we reset the variable
words = list(map(int, words))
print(words)
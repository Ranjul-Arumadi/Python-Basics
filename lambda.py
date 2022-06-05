'''
Lambda is anonymous function, no name, but has arguments
and expressions.

The higher order function reduce is used with lambda.

'''
from functools import reduce
values = [1,2,3,4]
#reduce(function, value-to-act-on)
#here our function is lambda function
a = reduce(lambda x,y: x+y, values)
print(a)
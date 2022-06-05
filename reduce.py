'''
TYpe of higher order function.

List of values -> apply function -> get single data value

Working :
---------

At first step, first two elements of sequence are picked and the result is obtained.
Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
This process continues till no more elements are left in the container.
The final returned result is returned and printed on console.

'''
from functools import reduce
values = [1,2,3]
def add(x,y):
    return x+y

a = reduce(add, values)
print(a)

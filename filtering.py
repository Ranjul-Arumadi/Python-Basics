'''
Also a higher order function.

We can def a function and use filter on a set of values
and the function we created to generate a list etc.
'''

#obj: apply filter on values list and make a new list
#the filtering is done based on the function we define

values = [1,2,3,4]

def odd(n):
    #return true if odd, false otherwise
    return n%2 == 1
a = list(filter(odd, values))

print(a)
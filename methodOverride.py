'''
Method overridding | Overridding __add__ and __str__
'''

class coordi(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    #            x  , y
    def __add__(self, t):
        return coordi(self.xt.x, self.y+t.y)
     
    def __str__(self):
        return "{"+str(self.x)+" , "+str(self.y)+"}"
        
    
a = coordi(1, 2) 
b = coordi(3,4)
c = a+b
print(c)
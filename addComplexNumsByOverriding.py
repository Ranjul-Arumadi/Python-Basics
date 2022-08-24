class complex(object):
    def __init__(self, r, c):
        self.r = r
        self.c = c
    def __add__(self, x):
        return complex(self.r+x.r, self.c+x.c)
        
    def __str__(self):
        return "{"+str(self.r)+"+"+str(self.c)+"i"+"}"
        
a = complex(3,4)
b = complex(1,2)
c = a+b
print(c)

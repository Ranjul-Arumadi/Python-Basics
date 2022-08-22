'''
__init__ is a magic function, acts as a constructor for a class.

self keyword represents an instance(object) of the given class.

Putting 'object' in class like...

class dog(object):
    
its only a practice and is not mandatory
'''

class dog(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print('Name is ', self.name, ' and age is ', self.age)
        
    def change_age(self):
        self.age = self.age+2
        
    def add_weight(self, weight):
        self.weight = weight

lucy = dog('Lucy', 30)
lucy.display()
lucy.change_age()
lucy.display()
lucy.add_weight(50)

print("Age only is ", lucy.age)
print("Weight is ", lucy.weight)
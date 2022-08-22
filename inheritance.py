'''
Inheritance 
'''

class dog(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print('Name is ', self.name, ' and age is ', self.age)
        
    def talk(self):
        print("bark!")


class cat(dog):
    
    def __init__(self, name, age, color):
        super().__init__(name, age)
        '''
            using super() we get all the stuff of the og class and if we want we can add more in our cat class
            becuz of super() the initilztn of name and age is already done and we need not do it again
        '''
        self.color = color
    
    def talk(self):
        print("meow!")
    '''
        Overriding the talk present in dog class
    '''
        
ola = cat('alex', 34, 'white')
ola.display()   
ola.talk()
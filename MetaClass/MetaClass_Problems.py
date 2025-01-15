'''
Create a metaclass that automatically adds a greet method to any class that uses it. 
The greet method should print "Hello, I am [class_name]".
'''
print('TASK 1 ')
class AutoGreet(type):
        
    def __new__(cls,name,base,attrs):
        def greet(self):
            print('Hello My name is {name}')
            
        attrs['greet'] = greet
        
        return super().__new__(cls,name,base,attrs)

class Greet(metaclass = AutoGreet):
    pass 

obj = Greet()
obj.greet()


'''
Create a metaclass that logs each time a method of a class is called. 
The log should print the method name and the arguments passed to it.
'''

print('TASK 2 ')
class LogMeta(type):
    def __new__(cls,name,base,attrs):
        attrs['greet'] = lambda self : print(f'Hello {self.name}')
        return super().__new__(cls,name,base,attrs)

class new_log_class(metaclass = LogMeta):
    def __init__(self,name):
        self.name = name  

obj = new_log_class('Ndk')
obj.greet()


'''
Create a metaclass that tracks the number of instances created for any class. When you create a new instance, 
the metaclass should keep track and print the number of instances for that class.
'''

class TrackMeta(type):
    def __new__(cls,name,base,attrs):
        attrs['count'] = 0
        return super().__new__(cls,name,base,attrs)
    
    def __call__(cls,*args,**kwargs): # cls is created class [ class1 or class2 ]
        cls.count+=1
        print(f'Instnace of {cls.__name__} created Total : {cls.count}')
        return super().__call__()
    
class class1(metaclass = TrackMeta):
    pass
class class2(metaclass = TrackMeta):
    pass

a1 = class1()
a2 = class2()

a3 = class2()
a4 = class1()


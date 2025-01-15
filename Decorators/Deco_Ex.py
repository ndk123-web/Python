from collections import deque
'''
1 -> Using Decorator As Function bases 
'''

def log_decorator(func):
    def wrapper(*args,**kwargs):
        print('Calling Add Function')
        res = func(*args,**kwargs)
        print('Addition is ',res)
    
    return wrapper


class myclass:
    
    @log_decorator      # add = log_decorator(add)
    def add(self,*args,**kwargs):
        t = 0
        for i in args:
            t+=i
        return t 

obj = myclass()
obj.add(1,2,3,4,5)


'''
2 -> class bases decorator
'''

def func(cls):
    cls.x = 5
    print('Attribute Added X : ',end="")
    return cls  

@func   # myclass = func(myclass) ->  which returns new myclass object which has x attribute
class myclass():
    pass

print(myclass.x)

'''
3 -> Chaining Decorator 
'''

def decorator1(func):
    def wrapper(*args,**kwargs):
        print('Decorator 1')
        return func(*args,**kwargs)
        
    return wrapper 

def decorator2(func):
    def wrapper(*args,**kwargs):
        print('Decorator 2')
        return func(*args,**kwargs)
    
    return wrapper

@decorator1 # call = decorator1(call) 
@decorator2 # call = decorator2(decorator1(call))  
def call():
    print('Hello its call')
    
'''
first prints decorator 1
'''

# call = decorator1(decorator2(call))
call()
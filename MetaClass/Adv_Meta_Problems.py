class Meta(type):
    
    _instances = {} 
    
    def __new__(cls,name,bases,dct):
        
        dct['__init__']= lambda self : print('Its Default Init class by Metaclass ')
        
        print('Creating new class using metaclass : ',cls.__name__)
        return super().__new__(cls,name,bases,dct)
    
    def __call__(cls,*args,**kwargs):
        
        if cls.__name__ not in cls._instances:
            instance = type.__call__(cls,*args,**kwargs)
            cls._instances[cls.__name__] = instance
            
        return cls._instances[cls.__name__]
            
            
class myclass(metaclass = Meta):
    pass

obj1 = myclass()
obj2 = myclass()

print(obj1 == obj2)
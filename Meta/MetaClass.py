class MyMeta(type):
    
    def __new__(cls, name, bases, attrs):
        print('Creating class:', name)
        
        copy = {}
        
        for k, v in attrs.items():
            if k.startswith('__'):
                copy[k] = v
            else:
                copy[k.upper()] = v
                
        return super().__new__(cls, name, bases, copy)
    
class Myclass(metaclass=MyMeta):
    x = 10
    y = 8

obj = Myclass()
print(obj.X)  # Accessing the attribute 'X' which was originally 'x'
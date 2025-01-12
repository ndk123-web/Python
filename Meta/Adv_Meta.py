class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print('Creating New Meta Class Object of Name:', name, 'and name of metaclass is', cls.__name__)
        print('Bases:', bases)
        print('dct:', dct)
        return super().__new__(cls, name, bases, dct)

    def __call__(cls, *args, **kwargs):
        print('Calling Meta Class Object of Name:', cls.__name__)
        return super().__call__(*args, **kwargs)

class MyClass(metaclass=MyMeta):
    def __init__(self, *args):
        self.args = args
        print('Initializing MyClass with arguments:', args)

print(type(MyClass))  # This will print the type of MyClass, which is MyMeta
MyClass(10, 20)  # This will call the __call__ method of MyMeta and then the __init__ method of MyClass
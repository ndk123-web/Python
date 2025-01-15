class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print('Creating Meta Class Object [ class ] :', name)
        return super().__new__(cls, name, bases, dct)

    def __call__(cls, *args, **kwargs):
        print('Creating Meta class object as [ instance ] :', cls.__name__)
        # Custom behavior before instance creation
        print('Arguments passed to __call__:', args, kwargs)
        instance = super().__call__(*args, **kwargs)
        # Custom behavior after instance creation
        print('Instance created:', instance)
        return instance

class MyClass(metaclass=MyMeta):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        print('Initializing MyClass with arguments:', self.args, self.kwargs)

# Instantiate MyClass
obj = MyClass(10, 20, key='value')
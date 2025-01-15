# Define a decorator function
def func(f):
    def wrapper(*args, **kwargs):
        # *args allows passing a variable number of positional arguments
        # **kwargs allows passing a variable number of keyword arguments
        print('Start')
        f(*args, **kwargs)  # Call the original function with its arguments
        print('End')
    return wrapper  # Return the wrapper function

''' equal to fun1 = func(fun1)  '''
@func  # Apply the decorator to fun1
def fun1(*args, **kwargs):
    print(f'Its Fun1 and args: {args} and kwargs: {kwargs}')

''' equal to fun2 = func(fun2) '''
@func  # Apply the decorator to fun2
def fun2(*args, **kwargs):
    print(f'Its Fun2 and args: {args} and kwargs: {kwargs}')


fun1(1,2,key='OP')
fun2(10)
import inspect
def check_one(x): #
    if x==1:
        def rv():
            print('It is 1 ')
    else:
        def rv():
            print('It is not 1')
    return rv # return memory address of the condition's rv()

fun = check_one(2)  # return memory address of the condition's rv()'
fun()   # calling function of that memory location

print(inspect.getsource(fun))
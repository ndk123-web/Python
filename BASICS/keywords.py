# Global

x = 100
def func():
    global x
    x =200
    print(x)

# func()

# Global

#NonLocal

def fun1():
    y = 'Jane'
    def fun2():
        nonlocal y
        y="Hello" 

    fun2()
    return y

# print(fun1())

#NonLocal
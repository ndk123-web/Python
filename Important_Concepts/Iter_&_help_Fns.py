import time

'''

end = ' ' is used to print the next print statement in the same line
sep = ' ' is used to separate the values in the print statement

'''

print('Hello','world',sep=" | ") # Hello | world
print('Yo',end=" ") # Yo and new line will not be printed

print() # It will print a new line

'''

for i in range(0,5):
    time.sleep(1)
    print(f'\r{i}',flush=True,end='') # It will print the value of i in the same line 
                                      # and also remove or flushes value of i 

'''

print("Hello\nWorld")  # Newline
print("Hello\tWorld")  # Horizontal Tab
print("Hello\rWorld")  # Carriage Return
print("C:\\Users\\Name")  # Backslash
print('It\'s a test')  # Single Quote
print("He said, \"Hello\"")  # Double Quote
print("Hello\bWorld")  # Backspace

'''

help - It is used to get the information about the function

'''
def test(a,b):
    '''
    I can document my function in comments
    it will be displayed when I use help function
    
    so what is happening ?
    test will receive 2 arguments and return sum of them
    '''
    a=1
    b=2
    return a+b 

print(help(print)) # It will give the information about the print function
print(help(test))   # It will give the information about the test function


'''

range - It is used to generate the sequence of numbers

'''

rng = range(2,10,2) # start, stop, step
print((rng))


'''
Iterable -> An object is said to be iterable if it can be used in a for loop (not having next method)
Iterator -> An object is said to be iterator if it can be used in a for loop and also has a next method (having next method)

Iterator -> 
    1. __iter__ -> It returns the iterator object itself
    2. __next__ -> It returns the next value of the sequence
    if any class has __next__ method then no need to convert iter() method because it is already an iterator
    
Iterable ->
    1. __iter__ -> It returns the iterator object itself
    
Iterable:
    Wo object jisme __iter__() method hota hai, jaise list, tuple, etc.
    For loop se directly elements ko iterate kiya ja sakta hai, without using next().

Iterator:
    Wo object jisme __next__() method hota hai.
    next() function ka use karke elements ko sequentially fetch karte hain.
    
Key Difference:
    Iterable objects mein __iter__() method hota hai jo ek iterator object return karta hai, aur aap for loop mein use karte hain.
    Iterator objects mein __next__() method hota hai jo elements ko manually iterate karne ke liye use hota hai.
'''

l = [1,2,3,4]
my_iterator = iter(l)
print(type(my_iterator))

for i in my_iterator: # It internally uses next() method
    print(i,end=" ")

while True:         # we manually need to call next() method 
    try:
        item = next(my_iterator)
        print(item,end=" ")
    except StopIteration:
        break 

print()
    
class MyIterator:
    def __init__(self,s,e):
        self.s=s 
        self.e=e 
    
    def __iter__(self):
        return self 
     
    def __next__(self):
        if self.s < self.e:
            num = self.s
            self.s+=1
            return num 
        else:
            raise StopIteration     # It will stop the iteration

Myobj = MyIterator(1,5)
my_iterator = iter(Myobj) # It will call __iter__ method
print(type(my_iterator))

while True:
    try:
        item = next(my_iterator)  # It will call __next__ method
        print(item,end=" ")
    except StopIteration:
        break 
    
print()

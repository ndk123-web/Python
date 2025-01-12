# All Methods , Functions , Variables , Iterators are Objects(instances)

'''

1. __init__(self):
    # Constructor method that gets called when an object is created from the class.
    # It initializes the attributes of the object.
    pass

2. __str__(self):
    # This method returns a string representation of the object.
    # It is called when the object is printed or converted to a string using str() or repr().
    pass

3. __del__(self):
    # This method is called when an object is about to be destroyed.
    # It is used to perform cleanup tasks, such as releasing resources or saving data.
    pass

4. __len__(self):
    # This method returns the number of items in the object.
    # It is called when the built-in len() function is called on the object.
    pass

5. __getitem__(self, index):
    # This method is called when the object is indexed using square brackets ([]).
    # It allows accessing elements of the object using index.
    pass

6. __setitem__(self, index, value):
    # This method is called when the object is indexed using square brackets ([]).
    # It allows modifying elements of the object using index.
    pass

7. __delitem__(self, index):
    # This method is called when the object is indexed using square brackets ([]).
    # It allows deleting elements of the object using index.
    pass

8. __call__(self, *args, **kwargs):
    # This method is called when the object is called as a function.
    # It allows the object to behave like a function.
    pass

9. __lt__(self, other):
    # This method is called when the object is compared to another object using the less than (<) operator.
    # It returns True if the object is less than the other object, and False otherwise.
    pass

10. __le__(self, other):
    # This method is called when the object is compared to another object using the less than or equal to (<=) operator.
    # It returns True if the object is less than or equal to the other object, and False otherwise.
    pass

11. __eq__(self, other):
    # This method is called when the object is compared to another object using the equal to (==) operator.
    # It returns True if the object is equal to the other object, and False otherwise.
    pass

12. __ne__(self, other):
    # This method is called when the object is compared to another object using the not equal to (!=) operator.
    # It returns True if the object is not equal to the other object, and False otherwise.
    pass

13. __gt__(self, other):
    # This method is called when the object is compared to another object using the greater than (>) operator.
    # It returns True if the object is greater than the other object, and False otherwise.
    pass

14. __ge__(self, other):
    # This method is called when the object is compared to another object using the greater than or equal to (>=) operator.
    # It returns True if the object is greater than or equal to the other object, and False otherwise.
    pass
    # This method is called when the object is used as a key in a dictionary.

15. __hash__(self):
    # This method is called when the object is used as a key in a dictionary.
    # It returns a hash value for the object, which is used for efficient dictionary operations.
    pass

16. __enter__(self):
    # This method is called when the object is used as a context manager using the 'with' statement.
    # It returns the object itself, allowing it to be used in a 'with' block.
    pass

17. __exit__(self, exc_type, exc_val, exc_tb):
    # This method is called when the object is used as a context manager using the 'with' statement.
    # It takes three arguments: exc_type, exc_val, and exc_tb.
    # It can perform cleanup tasks, such as closing a file or releasing resources, and return True to indicate that the exception was handled successfully.
    pass

18. __getattr__(self, name):
    # This method is called when the object does not have the requested attribute.
    # It allows the object to provide a default value for the attribute.
    pass


'''

a = 15
s = 'Hello'
l = [1,2,3]
def f():
    pass
print(type(a) , type(s) , type(l) , type(f) )
# Purpose is everything is object of some class that defines it's behavior

# Example 1
str1 = 'Hello'
str2 = 'World'

new_str = str1.__add__(str2)  # str1 + str2 is also same
print(new_str)

# Example 2
s = 'Hello Bro'
l = s.__len__() # len
l = len(s)
print(l)



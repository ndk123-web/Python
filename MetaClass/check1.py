'''
Each Class is an object of the "type" class
'''

''' This implicitly creates a class
'''
# class Person: 
#     pass 


''' This explicitly creates a class
'''
class foo:
    def fun():
        return 'hi'

# A method to add an attribute `z` to the object
def show_z(self):
    self.z = 19

# Using `type()` to create a class called `Person`
# Inherits from the `foo` class and defines its own attributes/methods
Person = type('Person', (foo,), {'x': 5, 'show_z': show_z})

# Adding an attribute `xy` to the class dynamically
Person.xy = 'Hello'

''' Accessing Using Class Attributes '''
print(Person.x)  # Accessing the class attribute `x`

''' fun() is inherited from the "foo" class '''
print(Person.fun())  # Calling the inherited static method `fun`

print(Person.xy)  # Accessing the dynamically added attribute `xy`

''' show_z() is a method of the `Person` class '''
Person_obj = Person()  # Creating an instance of `Person`
Person_obj.show_z()  # Calling `show_z` to add `z` to the instance
print(Person_obj.z)  # Accessing the instance attribute `z`

'''

1) Create a class Vector that represents a 2D vector with attributes x and y. Implement the __add__ method to add two vectors and return a new Vector object with the resulting x and y values.
Tasks:
Create two Vector objects.
Add them using the + operator and print the result.

'''

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Vector(self.x + other.x , self.y + other.y)

    def __str__(self):
        return f'Vector -> ({self.x}, {self.y} )'

v1 = Vector(1,2)
v2 = Vector(3,4)
v3 = Vector(5,6)
res = v1 + v2 + v3
print(res)

'''

Create a class CustomList that represents a list-like object. Implement the __getitem__ method to allow accessing elements of the list by index.

Tasks:
Create a CustomList object.
Access elements using indexing (e.g., obj[0]).

'''

class CustomList:
    def __init__(self,listt):
        self.data = listt

    def __getitem__(self, index):
        return self.data[index]

p = CustomList(listt=[1,2,3,4,5])
print(p[2])

'''

Create a class Person that has attributes name and age. Implement the __eq__ method to compare two Person objects for equality based on both name and age.

Tasks:
Create two Person objects.
Check if they are equal using the == operator.

'''

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __eq__(self,other):
        return self.name == other.name and self.age == other.age
    
    def __hash__(self):
        return hash(self.name)
    
    def __getitem__(self,index):
        if index == 0:
            return self.name
        elif index == 1:
            return self.age
        else:
            raise IndexError("Index out of range")
    
p1 = Person('Ndk',19)
p2 = Person('Ndk',29)

s = {p1,p2}
print('Len of s : ',len(s))

print(p1[0])
print(p1[1])

print(p2[0])
print(p2[1])


'''

Advance 

'''

class Adv_Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
        
    def __hash__(self):
        # returns hash value related to name when to append in set or dictionary
        return hash((self.name))  # hash of tuple of name and age
        
        # inside hash must me immutable object like string, tuple, int, float etc.
        

    def __eq__(self, other):
        # if two objects are in the same place, then __eq__ method of that object is called
        if self.name == other.name:
            if self.age != other.age:
                self.age = other.age  # Update the age to be the latest one
            return True  # Treat them as equal
        return False  # Not equal if names are different

# Creating objects
p1 = Adv_Person('ndk', 19)
p2 = Adv_Person('yash', 19)
p3 = Adv_Person('ndk', 20)

# Adding to the set
mydict = {p1, p2, p3}

# Printing the result
for i in mydict:
    print(i.name, i.age)


'''
Creating Hash able Objects
'''

class HASH:
    def __init__(self,li):
        self.li = li 
        self.hash = [0] * len(self.li)
    
    def hashing(self):
        for i in self.li:
            idx = i % len(self.li)
            if self.hash[idx] == 0:
                self.hash.insert(idx,[i])
            else:
                self.hash[idx].append(i)
    
    def __str__(self):
        return str(self.hash)

p1 = HASH([1,2,3,11])
p1.hashing()
print(p1)
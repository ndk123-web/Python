class Hash_Example:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __eq__(self,other):
        return self.name == other.name and self.age == other.age

    def __hash__(self):
        return hash( (self.name , self.age))


obj1 = Hash_Example('Ndk',18)
obj2 = Hash_Example('Ndk',18)

print(obj1 == obj2)

s = {obj1:'yo' , obj2:'op'}
print(s[obj2] == s[obj2])
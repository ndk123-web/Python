class Myclass:
    x=5
    def __init__(self, name, age):
      self.name = name
      self.age = age
      
    def __str__(self):
        return f"Myclass(name={self.name}, age={self.age})"
    
    def func_greet(self):
        return f"Hello {self.name} and you are {self.age} years old"
    
obj1 = Myclass(name="Navnath",age=19);

x=15
print(obj1)
print(obj1.name)
print(obj1.age)  
print('Outside Of Class Variable X :',x)
print('Inside Of Class Variable X :',obj1.x)
print('Inside Of Class Function :',obj1.func_greet())


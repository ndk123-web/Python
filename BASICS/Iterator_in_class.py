class Mynumber:
    def __iter__(self):
      self.a = 1
      return self
  
    def __next__(self):
        x = self.a
        self.a+=1
        return x
    
obj = Mynumber()
myit = iter(obj)        # calls __iter__ function one time 

for i in range(5):
    print(next(myit))   # calls __next__ function 5 times



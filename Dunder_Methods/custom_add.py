class Add():
    def __init__(self,val):
        self.val = val
    def __str__(self):
        return str(self.val)
    def __add__(self,other):
        if isinstance(other,Add):
            return Add(self.val * other.val) # return self anonymous() instead of self + other
        raise Exception("Invalid Type ")

obj1 = Add(10)
obj2 = Add(20)
obj3 = Add(30)

print(obj1 + obj2 + obj3)




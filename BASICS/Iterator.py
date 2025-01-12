import time


class custom_iter():
    def __init__(self,s,e):
        self.s = s
        self.e = e

    def __iter__(self):
        return self

    def __next__(self):
        if self.s < self.e:
            num = self.s
            self.s+=1
            return num
        else:
            raise StopIteration

obj = custom_iter(1,5)
for i in obj:
    print(i)
class custom_len_class():
    def __init__(self,s):
        self.s = s

    def __str__(self):
        return self.s

    def __len__(self):
        return len(self.s)-1

obj = custom_len_class('Hello')
print(len(obj))


class Stack:
    def __init__(self):
        self.stack=[]
        
    def push(self,val):
        self.stack.append(val)
    
    def pop(self):
        self.stack.pop()
        
    def peek(self):
        return self.stack[-1]
    
    def is_Empty(self):
        return len(self.stack)==0
        
    def display(self):
        for i in self.stack:
            print(i,end=" ")
        print()

class Oper:
    
    def __init__(self):
        self.s = Stack()
    
    def ans(self):
        while True:
            print('1.Push Item\n2.Pop Item\n3.Peek Item\n4.Display Stack\n5.Exit\nEnter Your Choice ')
            choice = int(input())

            match choice:
                case 1:
                    val = int(input("Enter value to push"))
                    self.s.push(val)
                    
                case 2:
                    if self.s.is_Empty():
                        print("Empty Stack")
                    else:    
                        self.s.pop()
                        print("Popped Successfully")
                
                case 3:
                    if self.s.is_Empty():
                        print("Empty Stack")
                    else:
                        print(self.s.peek())
                    
                case 4:
                    if self.s.is_Empty():
                        print("Empty Stack")
                    else:     
                        self.s.display()

                case 5:
                    print("Exiting")
                    break         

st = Oper()
st.ans()
class singlyNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
        
    def __str__(self):
        return str(self.val)
    
Head = singlyNode(1)
A = singlyNode(2)
B = singlyNode(3)
C = singlyNode(4)

Head.next = A
A.next = B
B.next = C

curr = Head
print("Singly LL")

while curr:
    print(curr.val,'->',end=" ")
    curr=curr.next
    
    
# DOUBLE LL
class doublyNode:
    def __init__(self,val,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev 
        
    def __str__(self):
        return f'{self.val}'
    
dHead = doublyNode(1)
dA = doublyNode(2)
dB = doublyNode(3)
dC = doublyNode(4)

dHead.next = dA
dA.prev = dHead
dA.next = dB
dB.prev = dA
dB.next = dC
dC.prev = dB

curr = dC 
print()
print("Doubly LL")

while curr:
    print(curr,'->',end=" ")
    curr=curr.prev 

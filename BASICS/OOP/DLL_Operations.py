class Doubly:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next 
        self.prev = prev 
        
    def __str__(self):
        return str(self.val)
    
class DLL:
    
    def ll(self):
        Head = None
        while True:
            print('\n1.Add Node at End\n2.Add Node at Start\n3.Delete Node at End\n4.Delete Node at Start\n5.Search Element\n6.Display Nodes\n7.Reverse Nodes\n8.Exit')
            choice = int(input("Enter your choice: "))
            
            match choice:
                
                case 1:  # Add node at the end
                    val = int(input('Add value at end: '))
                    new_node = Doubly(val)
                    
                    if Head is None:
                        Head = new_node
                    else:
                        curr = Head
                        while curr.next:
                            curr = curr.next 
                        curr.next = new_node
                        new_node.prev = curr  # Update the previous pointer of new node
                        
                case 2:  # Add node at the start
                    val = int(input('Add value at start: '))
                    new_node = Doubly(val)
                    
                    if Head is None:
                        Head = new_node
                    else:
                        new_node.next = Head
                        Head.prev = new_node  # Update the previous pointer of Head
                        Head = new_node
                    
                case 3:  # Delete node at the end
                    if Head is not None:
                        curr = Head
                        while curr.next:
                            curr = curr.next
                        if curr.prev:  # Check if the node is not the first node
                            curr.prev.next = None
                        else:
                            Head = None  # List becomes empty
                    else:
                        print('Empty list!')
                    
                case 4:  # Delete node at the start
                    if Head is not None:
                        Head = Head.next
                        if Head:  # If there is a new head, update its prev pointer
                            Head.prev = None
                    else:
                        print('Empty list!')
                        
                case 5:  # Search element
                    search = int(input("Enter value to be searched: "))
                    curr = Head
                    found = False
                    while curr:
                        if curr.val == search:
                            print("Found")
                            found = True
                            break
                        curr = curr.next
                    if not found:
                        print("Not Found")
                    
                case 6:  # Display nodes
                    if Head is None:
                        print("List is empty!")
                    else:
                        curr = Head
                        while curr:
                            print(curr, end=" <-> ")
                            curr = curr.next
                        print("None")
                    
                case 7:  # Reverse the nodes
                    if Head is None:
                        print("List is empty!")
                    else:
                        prev = None
                        curr = Head
                        while curr:
                            next_node = curr.next  # Store next node
                            curr.next = prev  # Reverse the next pointer
                            curr.prev = next_node  # Reverse the prev pointer
                            prev = curr  # Move prev to current node
                            curr = next_node  # Move curr to next node
                        Head = prev  # Set the last node as new head

                case 8:  # Exit the program
                    print("Exiting...")
                    break     


# Create the DLL instance and run the menu
LL = DLL()
LL.ll()

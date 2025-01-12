# Define the SinglyNode class that represents each node in the linked list
class SinglyNode:
    # Constructor method to initialize node with value and next pointer
    def __init__(self, val=None, next=None):
        self.val = val  # Store the value of the node
        self.next = next  # Store the reference to the next node (default is None)
    
    # String representation of the node (used for printing)
    def __str__(self):
        return str(self.val)  # Return the value of the node as a string

# Initially, the self.Head of the linked list is None, meaning the list is empty
class LinkedList:
        
    def __init__(self):
        self.Head = None
    
    def LL(self):
        # Start an infinite loop to display menu options
        while True:
            # Display the menu for user input
            print('1.Add Node\n2.Delete Node\n3.Search Node\n4.See All Nodes\n5.Exit\nEnter your choice')
            # Get the user's choice as an integer
            choice = int(input())

            # Use match-case (Python 3.10+) to handle the user's choice
            match choice:
                
                # Case 1: Add Node
                case 1:
                    # Get the value for the new node from the user
                    val = int(input("Enter Value: "))
                    # Create a new node with the given value
                    new_node = SinglyNode(val)
                    
                    # If the list is empty, make the new node the self.Head
                    if self.Head is None:
                        self.Head = new_node 
                    else:
                        # Traverse the list to find the last node
                        curr = self.Head
                        while curr.next is not None:
                            curr = curr.next
                        # Once the last node is found, link the new node to it
                        curr.next = new_node 

                # Case 2: Delete Node
                case 2:
                    # If the list is empty, display a message
                    if self.Head is None:
                        print("Empty Linked List")
                    else:
                        # If the list is not empty, remove the first node by updating self.Head
                        self.Head = self.Head.next

                # Case 3: Search Node
                case 3:
                    # Get the value to search for from the user
                    search = int(input('Enter value to search: '))
                    curr = self.Head
                    # Traverse the list to search for the node
                    while curr is not None:
                        # If the value is found, print "Found"
                        if curr.val == search:
                            print("Found")
                            break  # Exit the loop once the value is found
                        # If the value is not found, move to the next node
                        curr = curr.next
                    # If the loop ends without finding the value, print "Not Found"
                    if curr is None:
                        print("Not Found")

                # Case 4: See All Nodes
                case 4:
                    curr = self.Head
                    # If the list is not empty, traverse and print each node
                    if curr is None:
                        print("The list is empty.")
                    else:
                        # Loop through each node in the list and print it
                        while curr:
                            print(curr, '->', end=" ")
                            curr = curr.next
                        print("None")  # Indicate the end of the list

                # Case 5: Exit
                case 5:
                    # Print exit message and break the loop to stop the program
                    print('Exiting...')
                    break

ll = LinkedList()
ll.LL()
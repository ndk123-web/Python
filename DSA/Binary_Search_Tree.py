class Binary_search_tree:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.right = right
        self.left = left
        
    def insert(self,val,root):
        if not root:
            return
        
        new_node = Binary_search_tree(val)
        
        if val<root.val:
            if not root.left:
                root.left = new_node 
            else:
                self.insert(val,root.left,val)
        
        elif val>root.val:
            if not root.right:
                root.right = new_node
            else:
                self.insert(val,root.right)
        
                
                
    def display(self,root):
        if not root:
            return
        print(root.val,end=" ")
        self.display(root.left)
        self.display(root.right)
            
        
    
root = Binary_search_tree(10)
root.insert(20,root)
root.insert(30,root)
root.insert(6,root)
root.display(root)
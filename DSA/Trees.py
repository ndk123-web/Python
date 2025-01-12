from collections import deque

class TreeNode:
    def __init__(self,val,left=None,right=None ):
        self.left=left
        self.right = right
        self.val = val
        self.res = []
        
        
    def insert(self,val):
        if not self.left:
            self.left = TreeNode(val)
        else:
            # Logic for insert values sequentially
            q = [self]
            
            while q:
                node = q.pop(0)
                if node.left and node.right:
                    q.append(node.left)
                    q.append(node.right)
                else:
                    if not node.left:
                        node.left = TreeNode(val)
                    else:
                        node.right = TreeNode(val)
            # Logic for insert values sequentially
                        
    def pre_order(self,root):   # Node - Left - Right
        
        
        # if not root:
        #     return 
        # print(root.val,end=" ")
        # self.pre_order(root.left)
        # self.pre_order(root.right)
        
        stk = [root]
        
        while stk:
            node = stk.pop()
            print(node.val,end=" ")
            
            if node.right:
                stk.append(node.right)
            if node.left:
                stk.append(node.left)
            
        
    def post_order(self,root):  # Left - Right - Node
        if not root:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.val,end=" ")
        
    def in_order(self,root):    # Left - Node - Right
        if not root:
            return
        self.in_order(root.left)
        print(root.val,end=" ")
        self.in_order(root.right)
        
    def bfs(self,root):
        q = deque()
        q.append(root)
        
        while q:
            node = q.popleft()
            
            print(node.val,end=" ")
            
            if node.left : q.append(node.left)
            if node.right: q.append(node.right)
        
    def dfs(self,root,target):
        if not root:
            return False
        if root.val == target:
            return True 
        
        return self.dfs(root.left,target) or self.dfs(root.right,target)
        
        

root = TreeNode(10)
root.insert(20) 
root.insert(30)
print("Pre - Order : ",end=" ")
root.pre_order(root)
print()

print("Post - Order : ",end=" ")
root.post_order(root)
print()

print("In - Order : ",end=" ")
root.in_order(root)
print()

print("BFS : ",end=" ")
root.bfs(root)
print()

print("DFS : ",end=" ")
print(root.dfs(root,70))

class N_queen:
    def __init__(self,row,col):
        self.row = row 
        self.col = col 
        self.board = [[0 for c in range(col)] for r in range(row)]
        self.count = 0
    
    def is_safe(self,row,col):
        # For Same column
        for r in range(row):
            if self.board[r][col]==1:
                return False 
        
        # For upper left diagonal
        r,c = row,col
        while r>=0 and c>=0:
            if self.board[r][c]==1:
                return False
            r-=1
            c-=1
            
        # For Upper right diagonal
        for r,c in zip(range(row,-1,-1) , range(col,self.col)):
            if self.board[r][c]==1:
                return False 
        
        return True 
             
    
    def put_queen(self,row):
        if self.row == row:
            self.count += 1
            for r in self.board:
                print(r)
            print()
            return 
        
        for c in range(self.col):
            if self.is_safe(row,c):
                self.board[row][c]=1
                self.put_queen(row+1)
                self.board[row][c]=0 
    

# time complexity is O(n!) because we are using backtracking approach
# space complexity is O(n) for the extra space required for the board and count variable

r,c=4,4
queen = N_queen(r,c)
queen.put_queen(0)
print('Total number of solution : ',queen.count)
class Chaining_Hash:
    
    def __init__(self,size):
        self.size = size
        self.table = [ [] for _ in range(self.size) ]
        
    def generate_hash(self,key):
        return hash(key) % self.size 
    
    def insert(self,key,val):
        index = self.generate_hash(key)
        for pair in self.table[index]:
            if pair[0]==key:
                pair[1]=val
                return
        self.table[index].append([key,val])
    
    def delete(self,key):
        index = self.generate_hash(key)
        for pair in self.table[index]:
            if pair[0]==key:
                self.table[index].remove(pair)
                return
        return None 
    
    def search(self,key):
        index = self.generate_hash(key)
        for pair in self.table[index]:
            if pair[0]==key:
                return 'Found'
        return 'Not Found'
    
    def display(self):
        i = 0
        for table in self.table:
            i+=1
            print(f'Bucket {i} : ',end=" ")
            for pair in table:
                print(f'{pair[0]} : {pair[1]}',end=" | ")
            print()
            
obj = Chaining_Hash(4)
obj.insert('N1',10)
obj.insert('N2',20)
obj.insert('N3',30)
obj.insert('N4',40)

obj.display()
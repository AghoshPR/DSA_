class hashtable:
    
    def __init__(self,size=10):
        
        self.size = size
        self.buckets = [None]*size
        
        
    
    def hash_fun(self,key):
        
        return sum(ord(char) for char in key)%self.size
        
    
    def insert(self,key,value):
        
        index = self.hash_fun(key)
        
        original_index = index
        
        
        while self.buckets[index] is not None:
            
            if self.buckets[index][0] == key:
                self.buckets[index] = (key,value)
                return
            
            index = (index + 1) % self.size
            
            if index == original_index:
                raise Exception("Hash Table is full")
                
        self.buckets[index] = (key,value)
        
        
    def get(self,key):
        
        index = self.hash_fun(key)
        
        original_index = index
        
        
        while self.buckets[index] is not None:
            
            if self.buckets[index][0] ==key:
                return self.buckets[index][1]
                
            
            index = (index+1)%self.size
            
            if index == original_index:
                break
        return None
        
    
    def remove(self,key):
        
        index = self.hash_fun(key)
        
        original_index = index
        
        
        while self.buckets[index] is not None:
            
            if self.buckets[index][0] == key:
                
                self.buckets[index] = None
                return True
            
            index = (index+1) % self.size
            
            if index == original_index:
                break
        
        
        
        
        
        
        
    
    def display(self):
        
        for i,bucket in enumerate(self.buckets):
            print(f'index {i} value {bucket}')

h=hashtable()
h.insert('name','aghosh')
h.insert('amen','colision handled')
h.insert('aplace','colision handled')
h.insert('v','colision handled')

h.insert('age',23)
h.remove('age')
h.display()

print(h.get('name'))
            
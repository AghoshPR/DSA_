
class hashtableChaninig:
    
    
    def __init__(self,size=10):
        
        self.size = size
        self.buckets=[None]*size
        
        
    def hash_fun(self,key):
        
        return sum(ord(char) for char in key)%self.size
        
        
    
    def insert(self,key,value):
        
        index = self.hash_fun(key)
        
        if self.buckets[index] is None:
            self.buckets[index] = []
            
        
        for i,pair in enumerate(self.buckets[index]):
            
            if pair[0] == key:
                self.buckets[index][i] = (key,value)
                return
            
        
        self.buckets[index].append((key,value))
        
        
    def get(self,key):
        
        index = self.hash_fun(key)
        
        
        if self.buckets[index] is not None:
            
            for pair in self.buckets[index]:
                if pair[0] == key:
                    return pair[1]
                    
        return  None
        
    
    
    def remove(self,key):
        
        index = self.hash_fun(key)
        
        if self.buckets[index] is not None:
            
            for i,pair in enumerate(self.buckets[index]):
                
                if pair[0] == key:
                    del self.buckets[index][i]
                    return True
                    
    
    def display(self):
        
        
        for i,k in enumerate(self.buckets):
            
            print(f'index {i} value {k}')


                
v=hashtableChaninig()
v.insert('name','aghosh')
v.insert('same','aghosh')
v.display()



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


class HashTableQuadratic:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [None] * size

    def hash_fun(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        index = self.hash_fun(key)
        i = 1
        original_index = index

        while self.buckets[index] is not None:
            if self.buckets[index][0] == key:
                self.buckets[index] = (key, value)
                return
            index = (original_index + i ** 2) % self.size
            i += 1
            if i == self.size:
                print("Table is full")
                return
        self.buckets[index] = (key, value)

    def get(self, key):
        index = self.hash_fun(key)
        i = 1
        original_index = index

        while self.buckets[index] is not None:
            if self.buckets[index][0] == key:
                return self.buckets[index][1]
            index = (original_index + i ** 2) % self.size
            i += 1
            if i == self.size:
                break
        return None

    def remove(self, key):
        index = self.hash_fun(key)
        i = 1
        original_index = index

        while self.buckets[index] is not None:
            if self.buckets[index][0] == key:
                self.buckets[index] = None
                return True
            index = (original_index + i ** 2) % self.size
            i += 1
            if i == self.size:
                break
        return False

    def display(self):
        for i, v in enumerate(self.buckets):
            print(f"Index {i}: {v}")



       
class doubleHashtable:
    
    
    def __init__(self,size=10):
        
        
        self.size = size
        self.buckets = [None]*size
        
    
    
    def hash_fun1(self,key):
        
        return sum(ord(char) for char in key)%self.size
        
    
    def hash_fun2(self,key):
        
        return 7 - (sum(ord(char) for char in key)% 7)
        
    
    
    def insert(self,key,value):
        
        index = self.hash_fun1(key)
        step = self.hash_fun2(key)
        
        i=0
        
        while self.buckets[index] is not None:
            
            if self.buckets[index][0] == key:
                
                self.buckets[index] = (key,value)
                
            
            i+=1
            index = (index+ i* step)%self.size
            
            if i==self.size:
                print('table full')
                return
        
        self.buckets[index] = (key,value)
    
    def get(self,key):
        
        index = self.hash_fun1(key)
        step = self.hash_fun2(key)
        
        i=0
        
        
        
        while self.buckets[index] is not None:
            
            if self.buckets[index][0] == key:
                
                return self.buckets[index][1]
            
            i+=1
            index = (index+i*step)%self.size
            
            if index == self.size:
                break
            
    
    def remove(self,key):
        
        index = self.hash_fun1(key)
        step  = self.hash_fun2(key)
        
        i=0
        
        while self.buckets[index] is not None:
            
            if self.buckets[index][0] == key:
                
                self.buckets[index] = None
                return
            
            i+=1
            index = (index+i*step)%self.size
            if index == self.size:
                break
            
    
    def display(self):
        
        for i, v in enumerate(self.buckets):
            print(f"Index {i}: {v}")
      


 
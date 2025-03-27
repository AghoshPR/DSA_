class Hashtable:
    
    def __init__(self,size=10):
        
        self.size = size
        self.buckets = [[] for _ in range(size)]
        
        
    def hash_function(self,key):
        
        return sum(ord(char) for char in key)%self.size
        
    
    def insert(self,key,value):
        
        index = self.hash_function(key)
        bucket = self.buckets[index]
        
        
        for i,(k,v) in enumerate(bucket):
            
            if k == key:
                bucket[i] = (key,value)
                return
            
        bucket.append((key,value))
        
        
    def get(self,key):
        
        index = self.hash_function(key)
        bucket = self.buckets[index]
        
        
        for k,v in bucket:
            
            if k == key:
                return v
                
        return None
        
        
        
    def remove(self,key):
        
        index = self.hash_function(key)
        bucket = self.buckets[index]
        
        for i ,(k,v) in enumerate(bucket):
            
            if k == key:
                del bucket[i]
                return
            
            
    def display(self):
        for i,bucket in enumerate(self.buckets):
            print(f'index {i}:{bucket}')
            
ht = Hashtable()

ht.insert("orange",100)

ht.display()

print("after getting")
print(ht.get('orange'))



        
class HashtableLinearProbing:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [None] * size  

    def hash_fun(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        index = self.hash_fun(key)

        
        while self.buckets[index] is not None and self.buckets[index][0] != key:
            index = (index + 1) % self.size

        
        self.buckets[index] = (key, value)

    def get(self, key):
        index = self.hash_fun(key)

        
        original_index = index
        while self.buckets[index] is not None:
            if self.buckets[index][0] == key:
                return self.buckets[index][1]
            index = (index + 1) % self.size
            if index == original_index:
                break 
        return None  

    def remove(self, key):
        index = self.hash_fun(key)

        
        original_index = index
        while self.buckets[index] is not None:
            if self.buckets[index][0] == key:
                self.buckets[index] = None
                return
            index = (index + 1) % self.size
            if index == original_index:
                break 

    def display(self):
        for i, bucket in enumerate(self.buckets):
            print(f'index {i}: {bucket}')



ht_linear = HashtableLinearProbing()
ht_linear.insert("name", "aghosh")
ht_linear.insert("age", 21)
ht_linear.display()



class HashtableQuadraticProbing:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [None] * size  

    def hash_fun(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        index = self.hash_fun(key)
        original_index = index
        i = 1

        
        while self.buckets[index] is not None and self.buckets[index][0] != key:
            index = (original_index + i**2) % self.size
            i += 1

        
        self.buckets[index] = (key, value)

    def get(self, key):
        index = self.hash_fun(key)
        original_index = index
        i = 1

        
        while self.buckets[index] is not None:
            if self.buckets[index][0] == key:
                return self.buckets[index][1]
            index = (original_index + i**2) % self.size
            i += 1
            if index == original_index:
                break 
        return None 

    def remove(self, key):
        index = self.hash_fun(key)
        original_index = index
        i = 1

        
        while self.buckets[index] is not None:
            if self.buckets[index][0] == key:
                self.buckets[index] = None
                return
            index = (original_index + i**2) % self.size
            i += 1
            if index == original_index:
                break  

    def display(self):
        for i, bucket in enumerate(self.buckets):
            print(f'index {i}: {bucket}')



ht_quadratic = HashtableQuadraticProbing()
ht_quadratic.insert("name", "aghosh")
ht_quadratic.insert("age", 21)
ht_quadratic.display()




class HashtableDoubleHashing:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [None] * size  

    def hash_fun(self, key):
        return sum(ord(char) for char in key) % self.size

    def secondary_hash(self, key):
        return 7 - (sum(ord(char) for char in key) % 7)

    def insert(self, key, value):
        index = self.hash_fun(key)
        step_size = self.secondary_hash(key)

        
        while self.buckets[index] is not None and self.buckets[index][0] != key:
            index = (index + step_size) % self.size

        
        self.buckets[index] = (key, value)

    def get(self, key):
        index = self.hash_fun(key)
        step_size = self.secondary_hash(key)
        original_index = index

        
        while self.buckets[index] is not None:
            if self.buckets[index][0] == key:
                return self.buckets[index][1]
            index = (index + step_size) % self.size
            if index == original_index:
                break 
        return None  

    def remove(self, key):
        index = self.hash_fun(key)
        step_size = self.secondary_hash(key)
        original_index = index

        
        while self.buckets[index] is not None:
            if self.buckets[index][0] == key:
                self.buckets[index] = None
                return
            index = (index + step_size) % self.size
            if index == original_index:
                break  

    def display(self):
        for i, bucket in enumerate(self.buckets):
            print(f'index {i}: {bucket}')



ht_double = HashtableDoubleHashing()
ht_double.insert("name", "aghosh")
ht_double.insert("age", 21)
ht_double.display()
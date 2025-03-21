class Hashtable:
    
    def __init__(self,size=10):
        
        self.size = size
        self.buckets = [[] for _ in range(size)]
        
        
    def hash_function(self,key):
        
        return hash(key) % self.size
        
    
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

ht.insert("name", "Aghosh")
ht.insert("age", 21)

ht.insert("country", "India")

ht.display()

print("after getting")
print(ht.get('name'))



        
            
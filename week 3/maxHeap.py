class maxHeap:
    
    def __init__(self):
        
        self.heap = []
        
    def insert(self,value):
        
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)
        
    
    def extract_max(self):
        
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
            
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root
        
    def peek_max(self):
        return self.heap[0] if self.heap else None
        
    
    def heapify_up(self,i):
        
        parent = (i-1)//2
        if i > 0 and self.heap[i] > self.heap[parent]:
            self.heap[i],self.heap[parent] = self.heap[parent],self.heap[i]
            self.heapify_up(parent)
            
    
    def heapify_down(self,i):
        
        largest  = i
        left = 2*i+1
        right = 2*i+2
        n = len(self.heap)
        
        
        if left < n and self.heap[left] > self.heap[largest ]:
            largest  = left
        
        if right < n and self.heap[right] > self.heap[largest ]:
            largest =right
        
        
        if largest  != i:
            
            self.heap[i],self.heap[largest ] = self.heap[largest ],self.heap[i]
            self.heapify_down(largest )
            
        
manh = maxHeap()
manh.insert(5)
manh.insert(3)
manh.insert(8)
manh.insert(2) 
manh.insert(13)  
        
print(manh.peek_max())     # ➜ 3
print(manh.extract_max())  # ➜ 3
print(manh.heap)        
        
        
        
        
        
        
    
    
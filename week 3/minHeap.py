class minHeap:
    
    def __init__(self):
        
        self.heap = []
        
    def insert(self,value):
        
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)
        
    
    def extract_min(self):
        
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
            
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root
        
    def peek_min(self):
        return self.heap[0] if self.heap else None
        
    
    def heapify_up(self,i):
        
        parent = (i-1)//2
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i],self.heap[parent] = self.heap[parent],self.heap[i]
            self.heapify_up(parent)
            
    
    def heapify_down(self,i):
        
        smallest = i
        left = 2*i+1
        right = 2*i+2
        n = len(self.heap)
        
        
        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest=right
        
        
        if smallest != i:
            
            self.heap[i],self.heap[smallest] = self.heap[smallest],self.heap[i]
            self.heapify_down(smallest)
            
        
minh = minHeap()
minh.insert(5)
minh.insert(3)
minh.insert(8)
minh.insert(2) 
minh.insert(13)  
        
print(minh.peek_min())     # ➜ 3
print(minh.extract_min())  # ➜ 3
print(minh.heap)        
        
        
        
        
        
        
    
    
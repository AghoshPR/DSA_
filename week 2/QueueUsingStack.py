
class QueueUsingStack:
    
    def __init__(self):
        
        self.s1 = []
        self.s2 = []
        
        
    def enqueue(self,data):
        
        self.s1.append(data)
        
    
    def dequeue(self):
        
        if not self.s1 and not self.s2:
            print("quesue is empty")
            return
        
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        print("deque",self.s2.pop())
        
        
    
    def display(self):
        
        print("Queue",list(reversed(self.s2))+self.s1)
        
        
print("\n--- Queue Using Stack ---")
queue = QueueUsingStack()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display()
queue.dequeue()
queue.display()
        
            
            
            
        
        
        
        

# 
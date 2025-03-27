class StackUsingQueue:
    
    
    def __init__(self):
        
        self.q1=[]
        self.q2=[]
        
        
    def push(self,data):
        
        self.q1.append(data)
        
    
    def pop(self):
        
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
            
        print("Poped",self.q1.pop(0))    
        self.q1,self.q2 = self.q2,self.q1
            
    
    def display(self):
        print("satck: ",self.q1)
        
print("--- Stack Using Queue ---")
stack = StackUsingQueue()
stack.push(10)
stack.push(20)
stack.push(30)

stack.pop()

stack.display()
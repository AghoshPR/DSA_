         
class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        

class Circular:
    
    def __init__(self):
        
        self.head  = None
        
        
    
    def enqueue(self,data):
        
        
        np=Node(data)
        if self.head is None:
            
            
            self.head = np
            self.head.next = self.head
        else:
            
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            
            temp.next = np
            np.next = self.head
        
    def dequeue(self):
        
        if self.head.next == self.head:
            self.head = None
            
        temp = self.head
        
        while temp.next != self.head:
            temp = temp.next
        temp.next = self.head.next
        self.head = self.head.next
        
            
    
    def display(self):
        
        temp = self.head
        while temp:
            print(temp.data,end='-->')
            temp = temp.next
            if temp==self.head:
                break
        
           
        

c=Circular()
c.enqueue(10)
c.enqueue(20)
c.enqueue(30)
c.dequeue()
c.display()
            
        
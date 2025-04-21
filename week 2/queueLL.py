

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        

class QueueUsingLL:
    
    def __init__(self):
        
        self.head = None
        
    
    
    def enque(self,data):
        
        nb = Node(data)
        
        if self.head is None:
            self.head = nb
            
        else:
            
            np=Node(data)
            temp = self.head
            
            while temp.next:
                temp = temp.next
            
            temp.next = np
               
    
    
    def dequeue(self):
        
        if self.head.next:
            self.head = self.head.next
            
    
    def display(self):
        
        temp = self.head
        
        while temp:
            
            print(temp.data,end='-->')
            temp = temp.next
            
    
q = QueueUsingLL()
q.enque(10)
q.enque(20)
q.enque(30)
q.enque(40)
q.enque(50)
q.dequeue()
q.dequeue()
q.dequeue()
q.display()

    
        
        
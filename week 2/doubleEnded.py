class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        


class DoubleQueue:
    
    def __init__(self):
        
        self.head = None
        
    
    
    def insertFirst(self,data):
        
        np = Node(data)
        
        if self.head is None:
            
            self.head = np
        
        else:
            
            np.next = self.head
            self.head = np
    
    def insertLast(self,data):
        
        ne=Node(data)
        
        temp = self.head
        
        while temp.next:
            temp = temp.next
        
        temp.next = ne
        
    
    def deleteFirst(self):
        
        if self.head.next:
            
            self.head = self.head.next
    
    def deleteLast(self):
        
        if self.head.next is None:
            self.head = None
            
        
        temp = self.head
        
        while temp.next.next:
            temp = temp.next
        temp.next =None
        
    
            
    def display(self):
        
        temp = self.head
        
        while temp:
            
            print(temp.data,end='-->')
            temp = temp.next
            
d=DoubleQueue()
d.insertFirst(10)
d.insertFirst(20)
d.insertLast(50)
d.deleteFirst()
d.deleteLast()
d.display()
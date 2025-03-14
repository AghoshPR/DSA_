class Node:
    def __init__(self,data):
        
        self.data = data
        self.next = None
        
    
    
class SLL:
    
    def __init__(self):
        self.head=None
        
    def add_end(self,data):
        
        
        ne=Node(data)
        if self.head is None:
            self.head = ne
            
        else:
            
            temp = self.head
            
            while temp.next:
                temp=temp.next
            ne.next = temp.next
            temp.next=ne
        
    def remove_duplicates(self):
        
        temp = self.head
        
        while temp and temp.next:
            
            if temp.data == temp.next.data:
                temp.next = temp.next.next
            else:
                
                temp = temp.next
                
    
    def display(self):
        
        temp = self.head
        
        while temp:
            print(temp.data,end='-->')
            temp = temp.next
sll=SLL()
sll.add_end(10)
sll.add_end(10)
sll.add_end(20)

sll.add_end(30)
sll.display()     
print('after remmove duplicates')
sll.remove_duplicates()
sll.display()
    
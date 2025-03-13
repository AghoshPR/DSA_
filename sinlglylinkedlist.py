class Node:
    
    def __init__(self,data):
        
        self.data = data
        self.next = None
        

class SLL:
    
    def __init__(self):
        self.head = None
        

    def add_begin(self,data):
        
        nb = Node(data)
        
        if self.head is None:
            self.head = nb
        else:
            
            nb.next = self.head
            self.head = nb
    
    def add_end(self,data):
        
        ne = Node(data)
        
        if self.head is None:
            self.head = ne
        else:
            
            temp = self.head
            
            while temp.next:
                temp = temp.next
            
            temp.next = ne
            
    def insert_pos(self,data,pos):
        
        np = Node(data)
        
        if self.head is None:
            self.head = np
        
        
        
        elif pos == 1:
            
            self.add_end(data)
            return 
        
        else:
            
            temp = self.head
            
            for _ in range(pos-2):
                
                if temp is None:
                    
                    print("out of range")
                    return
                temp = temp.next
                
            np.next = temp.next
            temp.next = np
                
              
    def delete_begin(self):
        
        if self.head is None:
            print("list is empty")
        
        else:
            
            self.head = self.head.next
    
    def delete_end(self):
        
        if self.head is None:
            print("List is empty")
        
        if self.head.next is None:
            self.head = None
            return
        
        temp = self.head
        
        while temp.next.next:
            
            temp = temp.next
        
        temp.next = None
            
    
    def delete_pos(self,pos):
        
        if pos ==1:
            self.delete_begin()
            return
        
        
        temp = self.head
        
        for _ in range(pos - 2):
            
            if temp.next is None:
                print(" pos out of range")
                return
            
            temp = temp.next
        
        temp.next = temp.next.next
        
            
    def display(self):
        
        temp = self.head 
        
        while temp:
            print(temp.data,end="-->")
            temp = temp.next
        print("None")
    
sll=SLL()
sll.add_end(30)

sll.add_begin(10)
sll.add_begin(20)
sll.insert_pos(60,2)
sll.display()
print("after deletion")
sll.delete_pos(3)

sll.display()
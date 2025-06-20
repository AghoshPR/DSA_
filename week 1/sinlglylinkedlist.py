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
            
    def add_pos(self,data,pos):
        
        np=Node(data)
        temp = self.head
        
        for _ in range(pos-2):
            
            temp = temp.next
        
        np.next = temp.next
        temp.next = np
        
        
    def del_begin(self):
        
        if self.head is None:
            print("List is empty")
            
        else:
            
            self.head = self.head.next
        
    
    def del_end(self):
        
        if self.head is None:
            print("list is empty")
        
        elif self.head.next is None:
            self.head=None
            
        else:
            
            temp = self.head
            
            while temp.next.next:
                temp = temp.next
            
            temp.next = None
            
    def del_pos(self,pos):
        
        if self.head is None:
            print("list is empty")
        
        
        elif pos==1:
            self.del_begin()
        else:
            
            temp = self.head
            
            for _ in range(pos-2):
                
                temp = temp.next
            
            temp.next = temp.next.next
        
        
    def del_value(self,val):
        
        if self.head.data == val:
            self.head = self.head.next
            
        
        temp = self.head
        prev = None
        
        while temp is not None and temp.data != val:
            prev = temp
            temp = temp.next
            
        if temp is None:
            print("Value not found")
        
        prev.next = temp.next 


    def middlevalue(self):
        
        slow=self.head
        fast=self.head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
        
        if slow:
            print('value is ',slow.data)
            
    def remove_middle(self):
        
        if self.head is None or self.head.next is None:
            self.head=None
            return
        
        slow=self.head
        fast=self.head
        prev=None
        while fast and fast.next:
            fast=fast.next.next
            prev=slow
            slow=slow.next
            
        prev.next=slow.next

    def rev(self):
    
        prev=None
        temp=self.head
        
        while temp:
            
            next_node=temp.next
            temp.next=prev
            prev=temp
            temp=next_node
            
        self.head=prev           
            
    def display(self):
        
        temp = self.head
        
        while temp:
            
            print(temp.data,end='-->')
            temp = temp.next
        print("None")
        
        
        
sll=SLL()
sll.add_begin(10)
sll.add_begin(20)
sll.add_end(30)
sll.add_end(40)
sll.add_end(50)

sll.display()

print("adter adding")
sll.add_pos(60,2)

sll.del_begin()
sll.del_end()
sll.del_pos(3)
sll.del_pos(2)
sll.display()
        
sll.rev()   
        
     
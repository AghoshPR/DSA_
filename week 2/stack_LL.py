class Node:
    
    def __init__(self,data):
        
        self.data = data
        self.next = None
        
        
class Stack:
    
    def __init__(self):
        
        self.top = None
        
    
    def push(self,data):
        
        nb = Node(data)
        
        if self.top is None:
            
            self.top = nb
            
        else:
            
            nb.next = self.top
            
            self.top = nb
            
    def remove(self):
        
        if self.top is None:
            print("stack is empty")
        
        else:
            
            temp = self.top
            
            self.top = temp.next
            temp =None
            
    def display(self):
        
        temp = self.top
        
        while temp:
            print(temp.data)
            temp = temp.next
        print(None)
        
        
stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

stack.display()

print("after deletion")

stack.remove()
stack.push(60)
stack.display()
            
            
            
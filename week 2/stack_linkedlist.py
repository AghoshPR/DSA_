class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
    
class stack:
    
    def __init__(self):
        self.top = None
        
        
        
    def push(self,item):
        np = Node(item)
        np.next = self.top
        self.top = np
        
        print(f'Added {item} to the stack')
        
        
    def pop(self):
        if self.top is None:
            print("stack is empty")
            
        else:
            
            temp = self.top.data
            self.top = self.top.next
            print(f"Remove  {temp} from stack")
            
    
    def display(self):
        
        
        if self.top is None:
            print("list is empty")
            
        else:
            
            print("Stack elements (top to bottom)")
            
            temp = self.top
            while temp:
                print(temp.data,end=" ")
                temp =temp.next
            print()
            
s= stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

s.pop()
s.display()

            
            
#while loop implementation

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
        
        
        
stack=Stack()
while True:
    
    print("1. Add\n2.Remove\n3.display\n4.Exit")
    
    choice = int(input())
    
    if choice == 1:
        
        data = int(input("Enter data to push"))
        stack.push(data)      
        
    elif choice == 2:
        stack.remove()
    
    elif choice == 3:
        print("Current stack")
        stack.display()
        
    elif choice == 4:
        print("Exited")
        break
        
    else:
        print("invalid entery try again")
        
        
            
            
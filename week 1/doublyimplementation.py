class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:

    def __init__(self):
        self.head = None

    def add_begin(self,data):

        nb = Node(data)

        if self.head is None:
            self.head = nb

        else: 
            nb.next = self.head
            self.head.prev = nb 
            self.head = nb

    def add_end(self,data):

        ne=Node(data)
        if self.head is None:
            self.head=ne
        
        else:

            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next=ne
            ne.prev = temp
                
                

    def display(self):

        if self.head is None:
            print("Linkedlist is empty")
        else:

            temp = self.head
            while temp:
                print(temp.data,end="-->")
                temp = temp.next
            print("None")

    def rev(self):
        
        temp = self.head
        
        prev=None
        
        while temp:
            
            next = temp.next
            temp.next = prev
            temp.prev = next
            prev = temp
            temp = next
            
        self.head = prev
    





dll=DLL()
dll.add_begin(10)
dll.add_begin(20)
dll.after_node(20,40)
dll.add_end(30)
dll.display()
print("after reverse")
dll.rev()


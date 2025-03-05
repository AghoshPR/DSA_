class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
    


class DLL:
    def __init__(self):
        
        self.head = None


    def display(self):

        temp = self.head

        while temp:
            print(temp.data,end="-->")
            temp=temp.next

L=DLL()

n1=Node(10)

L.head = n1
f
n2=Node(20)

n2.prev = n1
n1.next = n2

n3 = Node(30)

n3.prev = n2
n2.next = n3

L.display()
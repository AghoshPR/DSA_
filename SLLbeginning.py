class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

    
class SLL:

    def __init__(self):
        
        self.head = None

    def insert_begining(self,data):
        
        nb=Node(data)
        nb.next = self.head
        self.head = nb
    
    def insert_end(self,data):

        ne = Node(data)

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne

    def insert_postion(self,pos,data):
 
        np = Node(data)
        temp = self.head

        for i in range(1,pos - 1):
            temp = temp.next
        np.data=data
        np.next=temp.next
        temp.next=np



    def display(self):

        if self.head is None:
            print("List is empty")
        
        else:

            temp = self.head
            while temp:
                print(temp.data,end='-->')
                temp=temp.next
            print('None')

sll=SLL()
n = Node(200)
sll.head = n
n2=Node(500)
n.next = n2
sll.insert_begining(50)
sll.insert_end(550)
sll.insert_postion(2,1000)
sll.display()
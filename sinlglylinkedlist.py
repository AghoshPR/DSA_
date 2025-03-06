class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self,data):

        nb = Node(data)

        if self.head is None:
            self.head = nb
            self.tail =nb
        else:
            nb.next = self.head
            self.head = nb

    def insert_end(self,data):
        
        ne=Node(data)

        if self.head is None:
            self.head =ne
            self.tail = ne
        else:

            self.tail.next = ne
            self.tail = ne

    def insert_position(self,pos,data):

        np = Node(data)
        if pos ==1:
            self.insert_beginning(data)
            return

        temp = self.head
        for _ in range(1,pos - 1):
            if temp is None:
                print("Position is out of range")
                return 
            temp = temp.next
        np.next = temp.next
        temp.next = np

        if np.next is None:
            self.tail = np


    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
        print("None")

sll=SLL()

sll.insert_end(300)
sll.insert_beginning(5)
sll.insert_end(60)
sll.insert_position(4,350)
sll.insert_position(3,200)
sll.insert_position(3,500)
sll.insert_position(2,100)
sll.display()
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
            self.head = ne
            self.tail = ne
        else:
            self.tail.next = ne
            self.tail = ne

        


    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
        print("None")

sll=SLL()


sll.insert_beginning(5)
sll.insert_end(60)
sll.display()
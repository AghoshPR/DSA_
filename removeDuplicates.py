class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    

class SLL:
    def __init__(self):
        self.head = None
        self.tail =None

    
    def add_number(self,data):

        nb = Node(data)

        if self.head is None:

            self.head = nb
            self.tail = nb
        
        else:

            nb.next = self.head
            self.head = nb

    def insert_end(self,data):
        ne = Node(data)

        if self.head is None:
            self.head = ne
            self.tail = ne

        else:

            self.tail.next = ne
            self.tail = ne
    
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
            print(temp.data,end="-->")
            temp = temp.next
        print("None")

sll=SLL()
sll.insert_end(5)
sll.insert_end(10)
sll.insert_end(15)
sll.insert_end(25)
sll.insert_end(25)
sll.display()
print("after removing the duplicates")
sll.remove_duplicates()
sll.display()

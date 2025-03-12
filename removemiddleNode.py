class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail =None

    def add_begin(self,data):

        nb = Node(data)

        if self.head is None:
            self.head = nb
        else:
            nb.next=self.head
            self.head = nb
    
    def add_end(self,data):

        ne = Node(data)

        if self.head is None:
            self.head = ne
            self.tail = ne
        
        else:

            self.tail.next = ne
            self.tail =ne
    
    def remeove_middle(self):
        if not self.head or not self.head.next:
            self.head =None
            return 

        slow = self.head
        fast =self.head
        prev = None

        while fast and fast.next:

            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next



    def display(self):

        temp = self.head

        while temp:
            print(temp.data,end="-->")
            temp = temp.next
        print("None")

sll=LinkedList()
sll.add_end(300)
sll.add_end(20)
sll.add_end(500)
sll.add_begin(10)

sll.display()

sll.remeove_middle()
sll.display()
                    

    

        
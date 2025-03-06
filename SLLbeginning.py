class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None
        self.tail = None

    
    def add_begining(self,data):
        add=Node(data)

        if self.head is None:
            self.head = add
            self.tail = add
        else:
            add.next = self.head
            self.head = add

    def insert_end(self,data):
        ne = Node(data)

        if self.head is None:
            self.head = ne
            self.tail = ne
        else:

            self.tail.next =ne
            self.tail=ne

    def insert_position(self,data,pos):

        np = Node(data)

        if pos == 0:
            self.add_begining(data)
            return 
        
        temp = self.head

        for _ in range(pos - 1):
            if temp is None:
                print("Out of range")
                return
            temp = temp.next
        np.next = temp.next
        temp.next = np
            

    def display(self):
        temp = self.head

        while temp:
            print(temp.data,end="-->")
            temp=temp.next
        print("None")

sll = SLL()



sll.insert_end(700)

sll.add_begining(500)
sll.add_begining(600)
sll.add_begining(800)
sll.insert_position(40,1)

sll.display()

class Node:
    def __init__(self,data):
        
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        
        self.head = None
        self.tail = None


    def add_begining(self,data):

        nb = Node(data)

        if self.head is None:
            self.head = nb
            self.tail = nb
        
        else:

            nb.next = self.head
            self.head = nb

    def add_pos(self,pos,data):

        np=Node(data)

        if pos == 0:
            self.add_begining(data)
            return 

        else:

            temp =self.head

            for _ in range(pos -1):
                if self.head is None:
                    print("Out of range")
                    return
                temp = temp.next
            np.next = temp.next
            temp.next = np
    def remove_first(self):

        if not self.head:
            return

        self.head = self.head.next
    
    def remove_end(self):

        if not self.head:
            return
        
        if self.head == self.tail:
            self.head = self.tail = None
            return
        
        temp = self.head

        while temp.next != self.tail:
            temp = temp.next
        temp.next = None
        self.tail = temp
    
    def remove_pos(self,pos):

        if not self.head:
            return

        if pos == 0:
            self.remove_first()
            return
        
        temp = self.head

        for _ in range(pos-1):

            if not temp or not temp.next:
                return
            
            temp = temp.next
        temp.next = temp.next.next
        self.tail =temp
        


    def display(self):

        temp = self.head

        while temp:
            print(temp.data,end="-->")
            temp = temp.next
        print("None")



sll=SLL()
sll.add_begining(10)
sll.add_pos(0,45)
sll.add_begining(20)
sll.add_begining(30)
sll.add_begining(40)
sll.display()
sll.remove_first()
sll.remove_end()
sll.remove_pos(2)
sll.display()



        
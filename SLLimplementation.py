class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class SinglyLL:

    def __init__(self):
        self.head = None

    def display(self):

        if self.head is None:
            print("Linked list is empty")
        else:

            temp = self.head
            while temp:
                print(temp.data,end='-->')
                temp = temp.next

run=SinglyLL()
n=Node(10)
run.head=n
n2=Node(40)
n.next=n2

n3=Node(100)
n2.next=n3
run.display()


            
    
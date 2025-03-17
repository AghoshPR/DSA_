class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
         self.head = None
         self.tail = None


    def arr_linked(self,arr):

        if not arr:
            return None
        
        self.head = Node(arr[0])
        temp = self.head


        for item in arr[1:]:
            temp.next = Node(item)
            temp = temp.next
        
        return self.head
    
    def reverse(self):

      prev = None

      temp =self.head

      self.tail = self.head

      while temp:

        new_node = temp.next
        temp.next = prev
        prev = temp
        temp = new_node

      self.head = prev
    

    def display(self):

        temp = self.head
        while temp:
            print(temp.data,end="-->")
            temp = temp.next
        print("None")

li=[2,3,4,5,6]

ll=SLL()
ll.arr_linked(li)
ll.display()
print("after reverse")
ll.reverse()
ll.display()


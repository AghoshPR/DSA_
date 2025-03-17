def bs(arr,target,low,high):
    
    if low > high:
        return -1
        
    mid = (high+low)//2
    
    
    if arr[mid]==target:
        return mid +1
    elif arr[mid]<target:
        return bs(arr,target,mid+1,high)
    else:
        return bs(arr,target,low,mid -1)
        
arr=[1,2,3,4,5]
target=4

print(bs(arr,target,0,len(arr)-1))
        
        
class Node:
    
    def __init__(self,data):
        
        self.data=data
        self.next = None
    
class SLL:
    def __init__(self):
        
        self.head = None
        
        
    
    def add_begin(self,data):
        
        
        nb=Node(data)
        if self.head is None:
            self.head = nb
        
        else:
            
            nb.next = self.head
            self.head = nb
            
    def add_end(self,data):
        
        
        ne = Node(data)
        
        temp = self.head
        
        while temp.next:
            
            temp = temp.next
        temp.next = ne
        
        
        
            
    def delete_begin(self):
        
        if self.head is None:
            print("the list is empty")
        else:
            
            self.head = self.head.next
            
    def rev(self):
        
        temp = self.head
        prev=None
        
        
        while temp:
            
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        self.head = prev
        
    def middle(self):
        
        if self.head is None:
            
            print("List is empty")
            
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        print("middle is ",slow.data)
            
            
    def display(self):
        
        
        temp = self.head
        
        while temp:
            
            print(temp.data,end="-->")
            temp=temp.next
        print("None")
        
        
sll=SLL()
sll.add_begin(10)
sll.add_begin(20)
sll.add_begin(30)
sll.add_begin(40)
sll.add_end(60)

sll.display()

print("after reverse")
sll.rev()
sll.display()
sll.middle()

            
        
        
        
        
        
        
        
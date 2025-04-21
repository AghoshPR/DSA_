s='malayalam'


f={}


for i in s:
    if i in f:
        f[i]+=1
    else:
        f[i]=1





for k,v in f.items():
    
    
    if v==1:
        print(k)
        break
    







def quick(arr):
    
    if len(arr)<=1:
        return arr
        
        
    pivot = arr[-1]
    
    left = [ x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    return quick(left) +[pivot] + quick(right)
    
arr=[100,1,34,5,6]

print(quick(arr))




def merge(arr):
    
    
    if len(arr) > 1:
        
        
        mid = len(arr)//2
        
        left = arr[:mid]
        right = arr[mid:]
        
        
        left_side = merge(left)
        right_side = merge(right)
        
        
        i=j=k=0
        
        
        while i < len(left_side) and j < len(right_side):
            
            
            if left_side[i] < right_side[j]:
                
                
                arr[k] = left_side[i]
                i+=1
            
            else:
                
                arr[k] = right_side[j]
                j+=1
            k+=1
            
            
            
        while i < len(left_side):
            
            arr[k] = left_side[i]
            i+=1
            k+=1
            
        
        while j < len(right_side):
            arr[k] = right_side[j]
            j+=1
            k+=1
    
    return arr
    
arr=[400,200,500,2]
print(merge(arr))




class Node:
    
    
    def __init__(self,data):
        
        self.data=data
        self.next = None
        
class QueueLL:
    
    
    def __init__(self):
        
        self.head = None
        
        
        
    
    
    def insert(self,data):
        
        
        np=Node(data)
        if self.head is None:
            
            self.head = np
            
        
        else:
            
            temp = self.head
            
            
            while temp.next:
                
                temp=temp.next
            
            temp.next = np
            
            
    
    def remove(self):
        
        if self.head.next:
            self.head = self.head.next
            
        
    def display(self):
        
        
        temp = self.head
        
        
        while temp:
            
            
            print(temp.data,end='-->')
            temp=temp.next
            
        print()
        
q=QueueLL()
q.insert(10)
q.insert(20)
q.insert(30)
q.remove()
q.display()




s='aghosh'


queue=[]

rev=''

for i in s:
    queue.append(i)
    
while queue:
    rev+=queue.pop()

print(rev)






def selection(arr):
    
    
    for i in range(len(arr)):
        
        
        min_val = min(arr[i:])
        
        min_ind = arr.index(min_val,i)
        
        
        arr[i],arr[min_ind] = arr[min_ind],arr[i]
        
    return arr


arr=[56,34,2,12,5]
print(selection(arr))


def bubble(arr):
    
    count=0
    for i in range(len(arr)):
        
        for j in range(len(arr)-1):
            
            
            if arr[j] > arr[j+1]:
                
                
                arr[j],arr[j+1] = arr[j+1],arr[j]
                count+=1
                
    print(count)
                
    return arr
    
arr=[5,4,3,2,1]

print(bubble(arr))
    
    
    # https://visualgo.net/en
        
        
    
    

        
        
            
            
            
                







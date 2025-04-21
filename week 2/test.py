

stack=[10,20,30,40]


temp = []

while stack:
    temp.append(stack.pop())


print(temp)



queue=[100,200,300,400]


temp_queue=[]

while queue:
    temp_queue.append(queue.pop(0))


while temp_queue:
    queue.append(temp_queue.pop())

print(queue)




class hashtable:

    def __init__(self,size=10):
        
        self.size = size
        self.buckets = [ [] for _ in range(size) ]


    def hash_fun(self,key):

        total = sum(ord(char) for char in key)
        return total % self.size
    
    def insert(self,key,value):

        index = self.hash_fun(key)
        bucket = self.buckets[index]


        for i,(k,v) in enumerate(bucket):

            if k == key:
                bucket[i] = (key,value)
                return
            
        bucket.append((key,value))

    
    def get(self,key):

        index = self.hash_fun(key)
        bucket = self.buckets[index]


        for k,v in bucket:
            if k==key:
                return v
            
        return None
    
    def remove(self,key):

        index = self.hash_fun(key)
        bucket = self.buckets[index]


        for i,(k,v) in enumerate(bucket):

            if k==key:
                del bucket[i]
                return
            
    def display(self):

        for i,bucket in enumerate(self.buckets):
            print(f'index: {i} value:{bucket}')


ht = hashtable()


ht.insert("name", "Aghosh")
ht.insert("age", 21)
ht.insert("country", "India")
ht.insert("mane", "Collision Test")
ht.display()

print(ht.get('name'))
print(ht.get('mane'))


def palind(s):

    stack=[]

    for char in s:
        stack.append(char)

    
    rev=''

    while stack:
        rev += stack.pop()

    return s == rev

print(palind('malayalam'))


s='hailool'
f={}

for i in s:

    if i in f:
        f[i]+=1
    else:
        f[i]=1
print(f)




def rev(stack):
    stk=[]
    while stack:
        stk.append(stack.pop())
    return stk
stack=[1,2,3,4,5]
print(rev(stack))




def is_palindrome(s):
    return s == s[::-1]
    

def longest(s):
    
    for i in range(len(s)):
        
        suffix = s[i:]
        
        if is_palindrome(suffix):
            return suffix
    return ""

s='abcdcccdd'
print(longest(s))



def is_valid(s):
    
    stack = []
    
    hash_val = { ']':'[','}':'{',')':'(' }
    
    for i in s:
        if i in hash_val:
            top_element = stack.pop() if stack else '#'
            
            if hash_val[i] != top_element:
                return False
        else:
            stack.append(i)
    return not stack
    
s="()"
print(is_valid(s))
        

def flatten(arr):
    
    res=[]
    for item in arr:
        if isinstance(item,list):
            res.extend(flatten(item))
        else:
            res.append(item)
    return res
res=[1, [2, [3, 4], 5], 6]
print(flatten(res))            
            


def rev(stack):
    
    if not stack:
        return 
    temp = stack.pop()
    rev(stack)
    stack.insert(0,temp)

stack=[7,8,9,10]
rev(stack)
print(stack)
    
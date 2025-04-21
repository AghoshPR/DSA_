   
def insert_bottom(stack,item):
    
    if not stack:
        stack.append(item)
    
    else:
        
        top = stack.pop()
        insert_bottom(stack,item)
        stack.append(top)
        
        

def rev(stack):
    if stack:
        top = stack.pop()
        rev(stack)
        insert_bottom(stack,top)
        
stack=[9,7,6,5,4]

print(stack)

rev(stack)
print(stack)


def inserstion(arr):
    
    
    for index in range(1,len(arr)):
        
        current_element = arr[index]
        
        position = index
        
        
        while current_element < arr[position - 1] and position > 0:
            
            arr[position] = arr[position - 1]
            position -= 1
            
        arr[position] = current_element
        
    return arr


print(inserstion([31,56,7,98,12,45]))            
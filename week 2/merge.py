         
def merge(arr):
    
    if len(arr) > 1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]
    
    
        left_half = merge(left_half)
        right_half = merge(right_half)
        
        i = j = k =0
        
        while i < len(left_half) and j<len(right_half):
            
            if left_half[i] < right_half[j]:
                
                arr[k] = left_half[i]
                
                i += 1
            else:
                
                arr[k] = right_half[j]
                j += 1
            k += 1
            
            
            
            
        while i < len(left_half):
            
            arr[k] = left_half[i]
            i +=1
            k +=1
            
        while j < len(right_half):
            
            arr[k] = right_half[j]
            
            j+=1
            k+=1
            
    return arr
    
    
print(merge([54,34,56,7,8,67]))
        
s='aghosh'        

st=merge(list(s))
v=''.join(st)
print(v)


        
# | Type       | Complexity                   |
# | ---------- | ---------------------------- |
# | Best Case  | **O(n log n)**               |
# | Average    | **O(n log n)**               |
# | Worst Case | **O(n log n)**               |
# | Space      | **O(n)** (needs extra array) |

        
            
    
    
    
    
    
    
    
    
    
    
    
        
def quick(arr):
    
    if len(arr) <= 1:
        return arr
        
        
    pivot = arr[-1]
    
    left = [ x for x in arr[:-1] if x <= pivot]
    right = [ x for x in arr[:-1] if x > pivot]
    
    return quick(left) + [pivot] + quick(right)
    
print(quick([65,8,90,4,32]))

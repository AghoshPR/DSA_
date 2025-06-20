def quick(arr):
    
    if len(arr) <= 1:
        return arr
        
        
    pivot = arr[-1]
    
    left = [ x for x in arr[:-1] if x <= pivot]
    right = [ x for x in arr[:-1] if x > pivot]
    
    return quick(left) + [pivot] + quick(right)
    
print(quick([65,8,90,4,32]))



# | Type       | Complexity                                        |
# | ---------- | ------------------------------------------------- |
# | Best Case  | **O(n log n)**                                    |
# | Average    | **O(n log n)**                                    |
# | Worst Case | **O(n²)** (when pivot is always smallest/largest) |
# | Space      | **O(log n)** (recursive stack)                    |

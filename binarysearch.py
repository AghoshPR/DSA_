def binary_search(arr,target):
    
    low = 0
    high = len(arr)-1
    
    while low <= high:
        
        mid = (high+low)//2
        
        if arr[mid]==target:
            return mid+1
            
        elif arr[mid]<target:
            
            low = mid +1
        else:
            high = mid - 1
    return -1
    

arr=[1,2,3,4,5,6]
target=4

res=binary_search(arr,target)

if res != -1:
    print(f'position found at {res}')
    
else:
    print("positon not found")
    
    
def bs(arr,target,low,high):
    
    if low > high:
        return -1
        
    mid = (low+high)//2
    
    if arr[mid] == target:
        return mid+1
    elif arr[mid] < target:
        return bs(arr,target,mid+1,high)
    else:
        return bs(arr,target,low,mid - 1)
        
arr=[4,5,6,7,8]
target=7

print(bs(arr,target,0,len(arr)-1))
    
    
    
    
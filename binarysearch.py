def binary_search(arr,target):

    low = 0
    high = len(arr)-1

    while low <= high:

        mid =(high+low)//2

        if arr[mid] == target:
            return mid
    
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr=[45,6,74,34,76]
target=76

res=binary_search(arr,target)

if res != -1:
    print(f'Pos found at {res+1}')
else:
    print("not found")
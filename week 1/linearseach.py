def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

a=[1,2,3,4,5]
b = 1


res = linear_search(a,b)

if res != -1:
    print(f'pos found at {res+1}')
else:
    print("not found")
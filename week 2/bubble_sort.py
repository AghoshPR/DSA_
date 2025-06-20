
li=[22,42,12,45,67]

for i in range(len(li)-1):

    for j in range(len(li)-1):

        if li[j] < li[j+1]:

            li[j],li[j+1] = li[j+1],li[j]
            
print(li) 


# | Type       | Complexity                                                      |
# | ---------- | --------------------------------------------------------------- |
# | Best Case  | **O(n)** (when array is already sorted, with optimized version) |
# | Average    | **O(n²)**                                                       |
# | Worst Case | **O(n²)**                                                       |
# | Space      | **O(1)** (in-place)                                             |


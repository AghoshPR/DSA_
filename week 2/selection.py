#selection sort




li=[32,45,6,9,32,78,9]

lis=[34,23,12,45,66]

for i in range(len(li)):
    
    min_val = min(li[i:])
    
    min_ind = li.index(min_val,i)
    
    li[i],li[min_ind] = li[min_ind],li[i]
     
print(li)


for i in range(len(lis)-1):
    m_ind= i
    
    for j in range(i+1,len(lis)):
        if lis[j] < lis[m_ind]:
            m_ind = j
            
    if lis[i] != lis[m_ind]:
        lis[i],lis[m_ind] = lis[m_ind],lis[i]
        
print(lis)



# | Type       | Complexity          |
# | ---------- | ------------------- |
# | Best Case  | **O(n²)**           |
# | Average    | **O(n²)**           |
# | Worst Case | **O(n²)**           |
# | Space      | **O(1)** (in-place) |

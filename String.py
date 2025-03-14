# def remove_letter(s,letter):
    
#     if not s:
#         return ""
        
#     if s[0] == letter:
#         return remove_letter(s[1:],letter)
        
#     else:
        
#         return s[0] +remove_letter(s[1:],letter)

# s='welcome'
# remove='w'

# output=remove_letter(s,remove)

# print(output)



#dupicate finding


# def dupli(arr,idx=0,seen=set(),duplicates=set()):
    
#     if idx == len(arr):
#         return list(duplicates)
        
    
#     if arr[idx] in seen:
#         duplicates.add(arr[idx])
#     else:
#         seen.add(arr[idx])
        
#     return dupli(arr,idx + 1,seen,duplicates)
    
# print(dupli([1, 2, 3, 4, 2, 3, 5]))
def sum_ele(arr):
    
    if not arr or arr==0:
        return 0
    return arr[0]+sum_ele(arr[1:])
li=[1,5]
print(sum_ele(li))


def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fib(n-1)+fib(n-2)
    
print(fib(6))


def rev(s):
    
    if len(s)==0:
        return ""
        
    return s[-1]+rev(s[:-1])
    
print(rev("aghosh"))


def rem_char(s,char):
    
    if len(s)==0:
        return ""
        
    if s[0] == char:
        return rem_char(s[1:],char)
    
    return s[0] + rem_char(s[1:],char)
    
word = 'baloon'

char='l'

print(rem_char(word,char))
    
a='aghosh'

print(a[:-1])
    
    
    
    
    
    
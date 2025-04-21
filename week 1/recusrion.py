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
    

    
    
    
    


def sum_n(n):
    
    if n == 0:
        return 0
    
    return n + sum_n(n-1)

print(sum_n(5))


def rev_str(s):
    
    if len(s)==0:
        
        return ''
    
    return s[-1] + rev_str(s[:-1])

print(rev_str('aghosh'))


def fact(n):
    
    if n==0:
        return 1
    
    return n * fact(n-1)
print(fact(5))



def fibo(n):
    
    if n==1:
        return 1
    if n==0:
        return 0
        
    return fibo(n-1) + fibo(n-2)
    
print(fibo(5))



def is_even(n):
    
    if n== 0:
        return True
    if n==1:
        return False
        
    return is_even(n-2)

print(is_even(6))   


def sum_digits(n):
    
    if n==0:
        return 0
        
    return (n%10) + sum_digits(n//10)
    
print(sum_digits(35))



def rev_num(n,rev=0):
    
    
    
    if n==0:
        return rev
        
        
    return rev_num(n//10,rev*10+n%10)
    
    
print(rev_num(123))


def palin(p):
    
    if len(p) <= 1:
        return True
    
    return p[0]==p[-1] and palin(p[1:-1])
    
print(palin('aha'))
        
    
    


    

    
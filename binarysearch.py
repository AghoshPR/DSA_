l=list()

n = int(input("Enter the number "))

print(f'Enter {n} elements: ')

for i in range(n):
    c=int(input())
    l.append(c)
l.sort()

print(l)

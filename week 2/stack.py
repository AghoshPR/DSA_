stack = []

def push():
    element = int(input("Enter the element"))
    stack.append(element)
    print(stack)

def pop():
    if not stack:
        print("Stack is empty")
    else:
        stack.pop()
        print(stack)

while True:
 
    print("1.push\n 2.pop\n 3.delete \nEnter the choice")
    choice = int(input())

    if choice == 1:
        push()
    elif choice ==2:
        pop()
    elif choice ==3:
        print(stack)
        break
    else:
        print("invalid number")
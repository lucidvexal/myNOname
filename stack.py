stack=[]
while True:
    n=int(input("if user wants to input something press 1 if the user wants to get rid of an element press 2, enter 3 if you want to display the elements:"))
    if n==1:
        x=input("please enter something:")
        stack.append(x)

    elif n==2:
        stack.pop()
        
    elif n==3:
        print(stack)

    if input('Do You Want To Continue? ') != '1':
        break


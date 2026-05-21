def add(x,y):
    c=x+y
    print("Addition:",c) 
def sub(x,y):
    if(x>y):
        c=x-y
        print("Subtraction:",c)
    else:
        c=y-x
        print("Subtraction:",c)
def mul(x,y):
    c=x*y
    print("Multiplication:",c)
def div(x,y):
    if(x>y):
        c=x/y
        print("Division:",c)
    else:
        c=y/x
        print("Division:",c)
while True:
    print("""1).Addition
            2).Subtraction
            3).Multiplication
            4).Division
            5).Exit""")
    ch=int(input("Enter your choice"))
    if(ch==1):
        x=int(input("Enter 1st number for Addition:"))
        y=int(input("Enter 2nd number for Addition:"))
        add(x,y)
    elif(ch==2):
        x=int(input("Enter 1st number for Subtraction:"))
        y=int(input("Enter 2nd number for Subtraction:"))
        sub(x,y)
    elif(ch==3):
        x=int(input("Enter 1st number for Multiplication:"))
        y=int(input("Enter 2nd number for Multiplication:"))
        mul(x,y)
    elif(ch==4):
        x=int(input("Enter 1st number for Division:"))
        y=int(input("Enter 2nd number for Division:"))
        div(x,y)
    elif(ch==5):
        exit()
    else:
        print("Invalid Choice")
        
        


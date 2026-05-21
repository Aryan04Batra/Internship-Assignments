def max(a,b,c):
    if(a>b and a>c):
        print("A =",a,"is maximum")
    elif(b>a and b>c):
        print("B =",b,"is maximum")
    else:
        print("C =",c,"is maximum")
print("Program to find maximum of 3 numbers")
a=int(input("Enter first number A:"))
b=int(input("Enter second number B:"))
c=int(input("Enter third number C:"))
max(a,b,c)
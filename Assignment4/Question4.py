def fact(l):
    mul=1
    for i in range (1,l+1):
       mul=mul*i
    print("Factorial of :",l,"=",mul)
print("Program to give factorial of a number")
l=int(input("Enter the number you want to find factorial of:"))
fact(l)
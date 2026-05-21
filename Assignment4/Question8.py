def prime(n):
    if(n<=1):
        print("The number",n,"is not prime")
    for i in range(2,n):
        if(n%i==0):
            print("The number",n,"is not prime")
            break
    else:
        print("The number",n,"is prime")
print("Program to find whether a number is prime or not")
n=int(input("Enter the number:"))
prime(n)
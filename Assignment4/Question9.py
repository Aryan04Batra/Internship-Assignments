def case(s):
    U=0
    L=0
    for i in s:
        
        if(ord(i)>=65 and ord(i)<=90):
            U=U+1
        elif(ord(i)>=97 and ord(i)<=122):
            L=L+1
        else:
            print(i,"is not a string")
    print("Uppercase letter are:",U)
    print("Lowercase letter are:",L)

print("Program to print uppercase and lowercase:")
s=input("Enter the string")
case(s)


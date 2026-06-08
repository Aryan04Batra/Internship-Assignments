num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
print("1).Addition")
print("2).Subtraction")
print("3).Multiplication")
print("4).Division")
c=int(input("Enter your choice:"))
if(c==1):
    print("Addition:",num1+num2)
elif(c==2):
    print("Subtraction:",num1-num2)
elif(c==3):
    print("Multiplication:",num1*num2)
elif(c==4):
    print("Division:",num1/num2)
else:
    print("Choice not valid")

num=int(input("Enter the number:"))
num2=num
reverse=0
while(num!=0):
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
if(num2==reverse):
    print("The number is a palindrone")
else:
    print("The number is not palindrone")


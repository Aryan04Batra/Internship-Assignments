def rang(n):
    if(n>=0 and n<=100):
        print("The number",n,"lies in the range 0 to 100")
    else:
        print("The number",n,"is not in range 0 to 100")
print("Program to find if the number inputted lies in the range 0 to 100")
n=int(input("Enter the number to be checked:"))
rang(n)
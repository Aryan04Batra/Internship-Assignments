def even(l):
    print("The even numbers from list:",l,"are")
    for i in l:
        if(i%2==0):
            print(i)
        else:
            pass
print("Program to print even numbers from a list")
l=[]
n=int(input("Enter the number of elements you want to enter in the list:"))
for i in range(0,n):
    inp=int(input("Enter the element:"))
    l.append(inp)
even(l)
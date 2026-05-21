def lmul(l):
    mul=1
    for i in l:
       mul=mul*i
    print("Multiplication of all elements of list is:",mul)
print("Program to give multiplication of all elements of list")
l=[]
n=int(input("Enter the number of elements you want to enter in the list:"))
for i in range(0,n):
    inp=int(input("Enter the element:"))
    l.append(inp)
lmul(l)
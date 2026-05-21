def dlist(l):
    l1=[]
    for i in l:
        if(l.count(i)==1):
            l1.append(i)
        else:
            pass
    print("Distinct elements list:",l1)
print("Program to present disting elements of a list")
l=[]
n=int(input("Enter the number of elements you want to enter in the list:"))
for i in range(1,n+1):
    inp=input("Enter the element:")
    l.append(inp)
dlist(l)
    
            
            

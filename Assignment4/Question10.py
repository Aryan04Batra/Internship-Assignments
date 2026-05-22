#Write
file=open("try.txt","w")
file.write("This is a new file")
file.close()

#Read
file=open("try.txt","r")
for x in file:
    print(x)
file.close()

#Append
file = open("try.txt", "a")
file.write("This line is appended\n")
file.close()

#Reading the appended text
#Read
file=open("try.txt","r")
for x in file:
    print(x)
file.close()
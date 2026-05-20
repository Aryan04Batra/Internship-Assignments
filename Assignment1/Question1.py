name=input("Enter student name:")
cla=input("Enter class:")
sub1=int(input("Enter marks of subject 1:"))
sub2=int(input("Enter marks of subject 2:"))
sub3=int(input("Enter marks of subject 3:"))
sub4=int(input("Enter marks of subject 4:"))
sub5=int(input("Enter marks of subject 5:"))
tot=sub1+sub2+sub3+sub4+sub5
per=(tot/500)*100
print("Name-",name,"\tClass-",cla,"\tPercentage-",per,"%")
if(per>=60):
    print("Grade: A")
elif(per>=50 and per<60):
    print("Grade: B")
elif(per>=40 and per<50):
    print("Grade: C")
elif(per>=33 and per<40):
    print("Grade: D")
else:
    print("Grade: Fail")
import csv

with open("Address_Book.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Address", "Mobile", "Email"])


def details():
    name = input("Enter the name: ")
    add = input("Enter the Address: ")
    mob = input("Enter the mobile number: ")
    em = input("Enter the Email: ")
    l = [name, add, mob, em]
    wr(l)

def wr(l):
    # Use append mode
    with open("Address_Book.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(l)

while True:
    print("""
1). Enter Data
2). Exit
""")

    c = int(input("Enter your choice: "))
    if c == 1:
        details()
    elif c == 2:
        exit()
    else:
        print("Invalid Choice")
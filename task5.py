# 1. Write a program in Python to allow the error of syntax to be handled using exception handling.
try:
    eval('x===x')
except:
    print("You can't do that.")

# 2. Write a program in Python to allow the user to open a file by using the argv module. If the 
# entered name is incorrect throw an exception and ask them to enter the name again. Make sure 
# to use read only mode.

from sys import argv
progname, filename = argv
print("Name of the program:", progname)
print("Name of the file entered:", filename)

while True:
    try:
        my_file = open(filename)
        content = my_file.read()
        print(content)
        my_file.close()
        break

    except:
        retry = input("Invalid Name, enter Y to reenter file name ")
        if retry =="Y":
            filename = input("enter valid file name: ")
        else:
            break

# 3. Write a program to handle an error if the user entered a number more than four digits it should 
# return “The length is too short/long !!! Please provide only four digits”

inp = int(input("Enter a number: "))
try:
    if len(str(inp)) > 4 or len(str(inp)) < 4:
        raise Exception("The length is too short/long !!! Please provide only four digits")
    else:
        print("User entered exactly 4 numbers. Here's what user wrote:", inp)
except Exception as e:
    print(e)

# 4. Create a login page backend to ask users to enter the username and password. Make sure to 
# ask for a Re-Type Password and if the password is incorrect give chance to enter it again but 
# it should not be more than 3 times.

print("CAUTION!!! User will only get 3 tries to enter their correct login information.")
uname = input("Please enter your username: ")
password = input("Please enter your password: ")
chance = 0
while chance < 2:
    if uname == "hello" and password == "world":
        print("Welcome", uname)
    else:
        uname = input("Reenter your username: ")
        password = input("Reenter your password: ")
        chance += 1

# 6. Read doc.txt file using Python File handling concept and return only the even length string from 
# the file. Consider the content of doc.txt as given below:
fh = open("doc.txt", 'r')
content = fh.read()
for i in content.split():
    if len(i) % 2 == 0:
        print(i)
fh.close()
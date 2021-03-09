# 1. Create three variables in a single line and assign values to them in such a manner that each one ofthem belongs to 
# a different data type. 
# E.g. :a = 1,b = 2.01,c = 'string' 

a, b, c = 1, 2.2, "new variable"

# 2.Create a variable of type complex and swap it with another variable of type integer. 

a = 2 + 3j
b = 5
a, b = b, a
print(a)
print(b)

# 3.Swap two numbers using a third variable and do the same task without using any third variable.  

# Swapping by using three variables
a = 4
b = 6
temp = b
b = a
a = temp
print(a)
print(b)

# Swapping by without using three variables
a = 4
b = 6
a, b = b, a
print(a)
print(b)

# 4.Write a program that takes input from the user and prints it using both Python 2.x and Python 3.xVersion.  

inp = int(input("Enter a number: "))
print(inp)
inp = eval(raw_input("Enter a number:"))
print(inp)

# 5.Write a program to complete the task given below:Ask users to enter any 2 numbers in between 1-10 , 
# add the two numbers and keep the sum inanother variable called z. Add 30 to z and store the output 
# in variable result and print result as thefinal output.  

a = int(input("Enter a number between 1-10: "))
b = int(input("Enter a number between 1-10: "))

z = a + b
result = z + 30
print("Result is", result)

# 6.Write a program to check the data type of the entered values. 
# HINT: Printed output should say -The data type of the input value is : int/float/string/etc

a = eval(input("Enter anything: "))
print("The type of a is", type(a))

# 7.Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and 
# UPPERCASE.(Refer:https://capitalizemytitle.com/camel-case/)  
#upper camelcase
FirstNumber = 20

#lower camelcase
firstNumber = 40

# snake case
first_number = 60

# uppercase
FIRSTNUMBER = 80

# 8.If one data type value is assigned to ‘a’ variable and then a different data type value is assigned 
# to ‘a’again. Will it change the value? If Yes then Why?

# Yes, it will change the type of the variable because Python is dynamically typed language. Python does not require
# to declare the type of the varible, it automatically recognize the type of variable with the help of the value 
# in the runtime.
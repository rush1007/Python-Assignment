# 1. Write a program in Python to perform the following operation: 
# If a number is divisible by 3 it should print “Consultadd” as a string 
# If a number is divisible by 5 it should print “Python Training” as a string 
# If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as astring.

num = int(input("Enter a number: "))
if num % 5 == 0 and num % 3 == 0:
    print("Consultadd - Python Training")
elif num % 3 == 0:
    print("Consultadd")
elif num % 5 == 0:
    print("Python Training")
else:
    print("Number isn't divisible by 3 or 5.")

# 2. Write a program in Python to perform the following operator based task: 
# Ask user to choose the following option first: 
# If User Enter 1 - Addition 
# If User Enter 2 - Subtraction 
# If User Enter 3 - Division 
# If User Enter 4 - Multiplication 
# If User Enter 5 - Average 
# Ask user to enter two numbers and keep those numbers in variables num1 and num2 
# respectively for the first 4 options mentioned above. 
# Ask the user to enter two more numbers as first and second for calculating the average as soon as 
# the user chooses an option 5.At the end if the answer of any operation is Negative print a 
# statement saying “NEGATIVE” NOTE: At a time a user can only perform one action.

print("Enter 1 for Addition")
print("Enter 2 for Subtraction")
print("Enter 3 for Multiplication")
print("Enter 4 for Division")
print("Enter 5 to find Average")

user_inp = int(input("Enter a number: "))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter a second number: "))

if user_inp == 1:
    result = num1 + num2

elif user_inp == 2:
    result = num1 - num2

elif user_inp == 3:
    result = num1 * num2

elif user_inp == 4:
    result = num1 / num2

elif user_inp == 5:
    num3 = int(input("Enter third number: "))
    num4 = int(input("Enter fourth number: "))
    result = (num1 + num2 + num3 + num4) / 4

else:
    print("You entered wrong number. Please try again.")

if result < 0:
    print("NEGATIVE")
else:
    print(result)


# 3. Write a program in Python to implement the given flowchart: 

a, b, c = 10, 20, 30
avg = (a + b + c) / 3
print("Avg:", avg)

if avg > a and avg > b and avg > c:
    print("Avg is higher than a, b, and c")
elif avg > a and avg > b:
        print("Avg is higher than a, b")
elif avg > a and avg > c:
        print("Avg is higher than a, c")
elif avg > b and avg > c:
        print("Avg is higher than b, c")
elif avg > a:
        print("Avg is just higher than a")
elif avg > b:
        print("Avg is just higher than b")
elif avg > c:
        print("Avg is just higher than c")

#4.Write a program in Python to break and continue if the following cases occurs: 
# If user enters a negative number just break the loop and print “It’s Over 
# ”If user enters a positive number just continue in the loop and print “Good Going”

user_inp = int(input("Enter a number: "))
while True:
    if user_inp < 0:
        print("It's over")
        break
    else:
        print("Good Going")

#5. Write a program in Python which will find all such numbers which are divisible by 7
#  but are not a multiple of 5, between 2000 and 3200. 

for x in range(2000, 3200):
    if (x % 7 == 0) and (x % 5 != 0):
        print(x)
# 6. What is the output of the following code examples?

# Ans. 

# The first code will run into an error because an int object is not iterable. 

# The second code will run and will print the following lines:
# 0
# error
# 1
# error
# 2

# The third code will run into an error because keyword "Break" should be break.

# 7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.Expected output: 0 1 2 4 5
# Note: Use ‘continue’ statement

for x in range(7):
    if x == 3 or x == 6:
        continue
    print(x)

# 8. Write a program that accepts a string as an input from the user and calculate the number of digits 
# and letters. Sample input: consul72Expected output: Letters 6 Digits 2
letters = 0
digits = 0
inp = input("Enter a string: ")
for x in inp:
    if x.isalpha():
        letters += 1
    elif x.isdigit():
        digits += 1
    else:
        print("This is not a letter or a digit")
print("Letters:", letters)
print("Digits:", digits)

#9 Read the two parts of the question below: 
# Write a program such that it asks users to “guess the lucky number”. 
# If the correct number isguessed the program stops, otherwise it continues forever.
# Modify the program so that it asks users whether they want to guess again each time. 
# Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question 
# whether they want to continue guessing. The program stops if the user guesses the correct 
# number or answers “no”. (The program continues as long as a user has not answered “no” and 
# has not guessed the correct number)

lucky_num = 10
while True:
    guess = int(input("Guess the lucky number: "))
    if guess == lucky_num:
        print("Good guess")
        break
    else:
        answer = input("Do you want to continue? ")
        if answer == "no":
            break
        else:
            continue

# 10. Write a program that asks five times to guess the lucky number. Use a while loop and a 
# counter,such as While counter <= 5:print(“Type in the”, counter, “number”counter=counter+1 
# The program asks for five guesses (no matter whether the correct number was guessed or not). 
# If thecorrect number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”. 
# After the fifth guess it stops and prints “Game over!”.
count = 0
lucky_num = 10
while count <= 4:
    guess = int(input("Guess the lucky number: "))
    if guess == lucky_num:
        print("Good guess")
    else:
        print("Try again")
    count += 1
    if count == 5:
        print("Game over")
        break


#11. In the previous question, insert break after the “Good guess!” print statement. break will terminate 
# the while loop so that users do not have to continue guessing after they found the number. 
# If the userdoes not guess the number at all, print “Sorry but that was not very successful”.
count = 0
lucky_num = 10
while count <= 4:
    guess = int(input("Guess the lucky number: "))
    if guess == lucky_num:
        print("Good guess")
        break
    else:
        print("Try again")
    count += 1
    if count == 5 and guess != lucky_num:
        print("Sorry but that was not very successful")

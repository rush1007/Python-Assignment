# 1. Create a list of given structure and get the Access list as provided below:
x = [100, 200, 300, 400, 500, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 600, 700, 800]
y = []
print(x[5][0:4])
print(x[0::2])
print(x[::-1])
print(x[5][5][0])
print(y)

# 2. Create a list of thousand numbers using range and xrange and see the difference between each other.
r=range(1,100)

# python3 range is equivalent to xrange.

# 3. How Tuple is beneficial as compared to the list?

# Tuple is beneficial to List when you don't want the user to accidentally change the 
# values in the set. Tuples are faster than list

# 4. Write a program in Python to iterate through the list of numbers in the range of 
# 1 to 100 and print the number which is divisible by 3 and is a multiple of 2. 
for i in range(1, 100):
    if i % 3 == 0 and i % 2 == 0:
        print(i)

# 5. Write a program in Python to reverse a string and print only the vowel alphabet 
# if it exists in the string with their index.
string = "hello"
rev_str = string[::-1]
for i in rev_str:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        index = string.index(i)
        print(index, i)

# 6. Write a program in Python to iterate through the string “hello my name is abcde” 
# and print the string which is having an even length.
string = input("Enter your string: ")
sp = string.split(" ")
for i in sp:
    if len(i) % 2 == 0:
        print(i)

# 7. Write a program in python to print the pair of numbers whose sum is equal to the 
# result number that is let's say 8. x=[1,2,3,4,5,6,7,8,9,-1]
x=[1,2,3,4,5,6,7,8,9,-1]
for i in x:
    for j in x[1:]:
        if i+j==8:
            print(i, j)

# 8. Write a program in Python to complete the following task:
# Create two lists such as even_list and odd_list. 
# Ask user to enter a number in the range of 1,50 and make sure if the entered number is even, append it 
# to the even_list and if the entered number is odd append it to the odd_list. 
# Keep that in mind you can only add 5 items in each list. 
# Make sure once you enter all the5 elements, calculate the sum of the list and return the maximum of the list.
even_list = []
odd_list = []
even_sum = 0
odd_sum = 0
while(len(even_list) < 5 or len(odd_list) < 5):
    elem = int(input("Enter any number in the range of 1 and 50: "))
    if elem % 2 == 0:
        if len(even_list) >= 5:
            print("Even list already has 5 elements")
        else:
            even_list.append(elem)
    else:
        if len(odd_list) >= 5:
            print("Odd list already has 5 elements.")
        else:
            odd_list.append(elem)
for i in even_list:
    even_sum += i
for i in odd_list:
    odd_sum += i
print("Even list elements:", even_list)
print("Sum of even elements:", even_sum)
print("Maximum element in even list:", max(even_list))
print("Odd list elements:", odd_list)
print("Sum of odd elements:", odd_sum)
print("Maximum element in odd list:", max(odd_list))

# 9.Write a program to find out the occurrence of a specific character from an alphanumeric string.
# Sample input:12abcbacbaba344ab
# Expected output:a=5 b=5 c=2
dict_char = {}
string = input("Enter anything: ")
for i in string:
    if i.isalpha():
        if i in dict_char:
            dict_char[i] += 1
        else:
            dict_char[i] = 1
print(dict_char.items())

# 10. Generate and print another tuple whose values are even numbers in the given tuple(1,2,3,4,5,6,7,8,9,10).
even_tup = []
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for i in tup:
    if i % 2 == 0:
        even_tup.append(i)
print(tuple(even_tup))

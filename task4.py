# 1. Write a program to reverse a string. 
# Sample input:“1234abcd” 
# Expected output:“dcba4321”
inp = input("Enter your string: ")
rev = inp[::-1]
print("Reversed string:", rev)

# 2. Write a function that accepts a string and prints the number of uppercase letters and lowercase letters. 
# Sample input:“abcSdefPghijQkl” 
# Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12
upper = 0
lower = 0
inp = input("Enter your string: ")
for i in inp:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    else:
        print("This is not a letter.")
print("No. of Upper case character:", upper, "No. of Lower case characters:", lower)

# 3. Create a function that takes a list and returns a new list with unique elements of the first list.

def distinct(lst):
    new_list = list(set(lst))
    return new_list
print("Unique list:", distinct(lst=[1, 2, 3, 4, 5, 1, 2]))

# 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a 
# hyphen-separated sequence after sorting them alphabetically.

inp = input("Enter a string of hyphen-separated characters: ")
hyp = inp.split("-")
hyp.sort()
print("-".join(hyp))

# 5. Write a program that accepts a sequence of lines as input and prints the lines after making all characters
#  in the sentence capitalized.Sample input: Hello world Practice makes man perfect 
# Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT

inp = input("Enter the string: ")
print(inp.upper())

# 6. Define a function that can receive two integral numbers in string form and compute their 
# sum and print it in the console.
def add(a, b):
    return int(a) + int(b)
print(add("4", "5"))

# 7. Define a function that can accept two strings as input and print the string with the maximum 
# length in the console. If two strings have the same length, then the function should print both 
# the strings line by line.
def max_length(str1, str2):
    if len(str1) > len(str2):
        print(str1)
    elif len(str1) < len(str2):
        print(str2)
    else:
        print(str1, str2)
max_length("hello", "hello")

# 8. Define a function which can generate and print a tuple where the values are square of numbers 
# between 1 and 20 (both 1 and 20 included).

def func():
    return tuple([(lambda x: x ** 2)(x) for x in range(1, 21)])
print(func())

# 9. Write a function called showNumbers that takes a parameter called limit. It should print all the 
# numbers between 0 and limit with a label to identify the even and odd numbers.
# Sample input: show Numbers(3) (where limit=3) 
# Expected output: 0 EVEN1 ODD2 EVEN3 ODD

def showNumbers(limit):
    for i in range(limit + 1):
        if i % 2 == 0:
            print(i, "EVEN")
        else:
            print(i, "ODD")

# 10. Write a program which uses filter() to make a list whose elements are even numbers between 1and 20 (both included)
lst = list(filter(lambda i: i % 2 == 0, range(1, 21)))
print(lst)

# 11. Write a program which uses map() and filter() to make a list whose elements are squares of even numbers 
# in [1,2,3,4,5,6,7,8,9,10].Hints: Use filter() to filter even elements of the given list 
# Use map() to generate a list of squares of the numbers in the filtered list. Use lambda() to define anonymous functions.

lst = filter(lambda i: i % 2 == 0, range(1, 11))
maps = map(lambda s: s**2, lst)
print(list(maps))

# 12. Write a function to compute 5/0 and use try/except to catch the exceptions

def zero_div():
    try:
        x = 5 / 0
        return x
    except ZeroDivisionError:
        print("User tried to divide by 0.")
    except:
        print("Some other error occured.")
zero_div()

# 13. Flatten the list[1,2,3,4,5,6,7]into 1234567using reduce().
from functools import reduce

y=reduce(lambda a,b:10*a+b,[1,2,3,4,5,6,7])
print(y)

# 14. Write a program in Python to find the values which are not divisible by 3 
# but are a multiple of 7. Make sure to use only higher order functions.

lst = list(filter(lambda x: x % 3 != 0 and x % 7 == 0, range(0, 22)))
print(lst)

# 15. Write a program in Python to multiply the elements of a list by itself using a 
# traditional function and pass the function to map() to complete the operation.

def mul_list(num):
    return num * num

lst = [1,2,3,4,5,6]
mul = list(map(mul_list, lst))
print(mul)

# 16(i)
""" def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k) """

# Output of the above code is 2.

# 16(ii)

""" def a():
    try:
        f(x, 4)
    finally:
        print('after f')
        print('after f?')
a() """

#NameError: name 'f' is not defined  
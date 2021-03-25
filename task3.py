# 1. Create a list of 10 elements of four different data types like int, string, complex and float. 

lst = [1, "Hello", 3.2, 2+3j, "Consultadd", 4, 5.5, 4+9j, "Training", 20]
print(lst)

# 2. Create a list of size 5 and execute the slicing structure

lst = [1, 2, 3, 4, 5]
sli = lst[2:4]
print(sli)

# 3. Write a program to get the sum and multiply of all the items in a given list. 

lst = [1, 2, 3, 4, 5]
add = 0
multiply = 1

for i in range(len(lst)):
    add += lst[i]
print("Addition of all the numbers in the list:", add)

for i in range(len(lst)):
    multiply *= lst[i]
print("Multiplication of all the numbers in the list:", multiply)

# 4. Find the largest and smallest number from a given list.

lst = [25, 45, 15, 40, 55, 100, 1, 30, 20, 200, 0, 21, 25, -4]
max = 0
min = lst[0]
for i in range(len(lst)):
    if min > lst[i]:
        min = lst[i]
    if lst[i] > max:
        max = lst[i]
print("Max number in the list:", max)
print("Min number in the list:", min)

# 5.Create a new list which contains the specified numbers after removing the even numbers from a predefined list. 

odd_lst = []
lst = [1, 2, 3, 4, 5]
for i in range(len(lst)):
    if lst[i] % 2 != 0:
        odd_lst.append(lst[i])
print(odd_lst)

# 6. Create a list of elements such that it contains the squares of the first and last 5 elements between 1 and 30 (both included). 

lst = []
for i in range(1, 6):
    lst.append(i * i)
for i in range(26, 31):
    lst.append(i * i)
print(lst)

# 7. Write a program to replace the last element in a list with another list.Sample input: [1,3,5,7,9,10], 
# [2,4,6,8]Expected output: [1,3,5,7,9,2,4,6,8]

lst = [1, 3, 5, 7, 9, 10]
new_lst = [2, 4, 6, 8]
lst[-1:] = new_lst
print(lst)

# 8. Create a new dictionary by concatenating the following two dictionaries: # Sample input:a={1:10,2:20} 
# b={3:30,4:40}Expected output: {1:10,2:20,3:30,4:40}

a = {1: 10, 2: 20}
b = {3: 30, 4: 40}
a.update(b)
print(a)

# 9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1 and n(both 1 
# and n included). Sample input:n=5 Expected output: {1:1, 2:4, 3:9, 4:16, 5:25} 

x = {}
for i in range(1, 6):
    x[i] = i * i
print(x)

# 10. Write a program which accepts a sequence of comma-separated numbers from console and generates a list and a 
# tuple which contains every number in the form of string.
# Sample input: 34,67,55,33,12,98 
# Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)
lst = []
tup = ()
inp = input("Enter a string of number: ")
lst.append(inp)
tup = tuple(lst)
print(lst, tup)
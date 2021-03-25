# 1. Write a program in Python to find out the character in a string which is uppercase using list comprehension.
inp = "Hello... How are you?"
output = [i for i in inp if i.isupper()]
print("Uppercase characters in input", inp, "are", output)

# 2. Write a program to construct a dictionary from the two lists containing the names of students and 
# their corresponding subjects. The dictionary should map the students with their respective subjects. 
# Let’s see how to do this using for loops and dictionary comprehension.
students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']
zip_dict = dict(zip(students, subjects))
print(zip_dict)

# 4. Write a program in Python using generators to reverse the string. Input String = “Consultadd Training”
class gen:
    def reverse_string(my_str):
        length = len(my_str)
        var=my_str[::-1]
        print(var)

string = "ConsultAdd Training"
gen.reverse_string(string)

# 5. Write an example of decorator
def func(myfunc):
    def inner():
        print("Starting the decorator function")
        myfunc()
        print("Decorator ended")  
    return inner()
 
@func 
def dec_func():
    print("Called from the decorator function.")
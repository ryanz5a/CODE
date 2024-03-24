# regular function
# A function is a block of code that performs a specific task.


def greet():
    print("hello my name is Bryan")
greet()


## with arguments
# an argument is a value that is accepted by a function.
def add_numbers(a,b):
    sum = a + b
    print(' The sum of my function is: ',sum)
# add_numbers(12, 60)


def multiply_2numbers(a = 12, b = 2):
    mult = a * b
    print('mult', mult)
#multiply_2numbers()



def add_numbers( a = 7,  b = 8):
    sum = a + b
    print('Sum:', sum)


# function call with two arguments
# add_numbers(2, 3)

# #  function call with one argument
# add_numbers(a = 2)

# # function call with no arguments
# add_numbers()


# def display_info(first_name, last_name):

#     fullname = first_name + ' ' + last_name
#     print('My fullname is : ', fullname)
   
# display_info("Eric", "Smith")

# program to find sum of multiple numbers 

def find_sum(*numbers):
    result = 0
    
    for num in numbers:
        result += num
    
    print("Sum = ", result)

# function call with 3 arguments
find_sum(1, 2, 3)

# function call with 2 arguments
find_sum(4, 9)

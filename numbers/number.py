# numeric data type, int float complex


# Number Systems
# The numbers we deal with every day are of the decimal (base 10) number system.

# But computer programmers need to work with binary (base 2), 
# hexadecimal (base 16) and octal (base 8) number systems.

# In Python, we can represent these numbers by appropriately placing a prefix before that number. 
# The following table lists these prefixes.




# print(0b1101011)  # prints 107

# print(0xFB + 0b10)  # prints 253

# print(0o15)  # prints 13






# num1 = int(2.3)
# print(num1)  # prints 2

# num2 = int(-2.8)
# print(num2)  # prints -2

# num3 = float(5) # it is always going to evaluate as truthy
# #print(num3) # prints 5.0

# if num3:
#     print(True , type(num3))
# else:
#     print(False , type(num3))


# num4 = complex('3+5j')
# num5 = 2 + 3j
# print(type(num5))  # prints (3 + 5j)







# x = 1  # int
# y = 2.2 # float
# z = 1j  # complex


# print(type(x))
# print(type(y))
# print(type(z))

# access the 1st character.
languages = ('Python', 'Swift', 'C++')
print(languages[1])
print("Total lenght of our tuple is :", len(languages))

# Text Type:	str
# Numeric Types:	int, float, complex 
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType


#------------------------------------------------------------------ 0,1,2,3,4,5,6

# x = "Hello World"	str	
# x = 20	int	
# x = 20.5	float	
# x = 1j	complex	
# x = ["apple", "banana", "cherry"]	list	array  arr = [1,2,3,4]
# x = ("apple", "banana", "cherry")	tuple	
# x = range(6)	range	
# x = {"name" : "John", "age" : 36, "gender": "male"}	dict	
# x = {"apple", "banana", "cherry"}	set	
# x = frozenset({"apple", "banana", "cherry"}, {"kiwi", "mango", "avocado"})	frozenset	
# x = True	bool	
# x = b"Hello"	bytes	
# x = bytearray(5)	bytearray	
# x = memoryview(bytes(5))	memoryview	
# x = None	NoneType




# initial program, write to the console.
# declaring variable 

text1 = "my name is Dominique!"

#print(text1)




# This program adds two numbers

num1 = 1.5
num2 = 6.3

# Add two numbers
sum = num1 + num2

# Display the sum
#print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
print(sum)
#print(1+3+4)



# Store input numbers
# num1 = input('Enter first number: ')
# num2 = input('Enter second number: ')

# Add two numbers
# sum = float(num1) + float(num2)

# Display the sum
#print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))



#print('The sum is %.1f' %(float(input('Enter first number: ')) + float(input('Enter second number: '))))



# Python Program to calculate the square root

# Note: change this value for a different result
num = 8 

# To take the input from the user
#num = float(input('Enter a number: '))

num_sqrt = num ** 0.5
#print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))

##defining lists
numbers = list(range(20))
print(numbers)
chars = list("Hello Mike Doe")
print(chars)

#  We can also get the lenght
print(len(chars))

# Accessing Items
letters = ["a","b","c","d"]
letters[0]= "A"
print(letters)
print("ex2",letters[0:3])
print("ex3",letters[:3])


num = list(range(20))
print(num)


# return in reverse order
print(num[::-1])




## Add Item to a list

names = ["Sam", "Jimmy", "Joel", "Emily","David"]
# names.append("Fred")
# print(names)


## Add at a specific position
# names.append("Fred")
# names.insert(0, "`")
# print(names)


## removing object
# names.pop()
# print(names)

## remove at a specific position
#names.pop(0)

## remove a range of item
# del letters[0:3]
# print(names)

## clear everything 
letters.clear()
# loop over a list
letters = ["a", "b", "c"]

# for letter in letters:
#     print(letter)



# for letter in enumerate(letters):
#     print(letter)              # output a tuple (0, 'a') that is read only cannot something to it


# let's unpack this tuple
    # items = (0,  "a")
    # index, letter = items

for index, letter in enumerate(letters):
    print(index,letter)




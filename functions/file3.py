# # Sorting 

numbers = [3,51,5,10,4,20]
sortednumbersdesc = sorted(numbers, reverse=True)
sortednumbersasc = sorted(numbers, reverse=False)
# print("Ascending numbers",sortednumbersasc)
# print("Descending numbers",sortednumbersdesc)

# numbers.sort()
# print(numbers)


items = [
    ("Product1", 20),
    ("Product2", 70),
    ("Product3", 10),
    ("Product4", 9),
    ("Product5", 29),
]

# def sort_item(item):
#     return item[1]


# items.sort(key=sort_item, reverse=True)
# items.sort(key=sort_item, reverse=True)
# print(items)
# print(items)



# # lambda expression

# items.sort(key=lambda item: item[1])
# print(items)


# # map function

employees = [
      ("John", 34),
      ("max", 22),
      ("Jennifer", 27),
      ("Bill", 45),
      ("Ryan", 32),
      ("Ryan", 19),
      ("Ryan", 20),
      ("Ryan", 21),
   ]

# # using for loop
# ages = []
# for emp in employees:
#     ages.append(emp[1])

# print(ages)


# # using the map method
age = list(map(lambda emp: emp[1], employees))
# print("using map", age)

employees = [
      ("John", 34),
      ("max", 22),
      ("Jennifer", 27),
      ("Bill", 45),
      ("Ryan", 32),
      ("Ryan", 19),
      ("Ryan", 20),
      ("Ryan", 21),
   ]

# # how about we added filter method 


employeeagegreaterthan27 = list(filter(lambda age: age[1] <= 27, employees))

#print(employeeagegreaterthan27)



students = [
      ("John", 95),
      ("max", 88),
      ("Jennifer", 78),
      ("Bill", 90),
      ("Ryan", 80),
      ("Ryan", 75),
      ("Ryan", 84),
      ("Ryan", 100),
   ]

### return the list of students with a grade higher than 85.


###
   # Within this code block run result from line 83.
####

## Zip function
subject1 = [3,9,10,23]
subject2 = [11,23,45,10]


#print(list(zip(subject1, subject2)))




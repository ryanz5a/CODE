## we have 2 types of functions
# functions that perform a task
# function that return a value


# def greet(name):
#     print(f"Hi {name}")


# greet("Samuel")


# def build_puzzle(piece, number):
#     return f"Hello I have {piece} {number}  available"


# result = build_puzzle(23, "square")
# print(result)



# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total  


# # print(multiply(1,2,3,5))

def grade_average(*numbers):
    total = 1
    for number in numbers:
        total += number
       
    return total / 5


print(grade_average(92,94,96,89,100))



def grocery_price(*groceries):
    total = 1
    
    for groc in groceries:
        total += groc 
        # after tax
        aftertax = ((total * .0825) + total)

    return total, aftertax


print(grocery_price(10,10,5,4,3))


# As a Software Engineer, you make $120k yearly.You contribute $3500 in 401K and you pay $3000 for medicare. 
# At a 12% tax rate, what is your net salary?


def salary_check():
    salary = 120000
    Contri = 3500
    med = 3000
    taxable_salary =14400
    expenses = Contri + med +taxable_salary
    net_sal = salary - expenses
    return net_sal



print(salary_check())



# ** args
def save_users(**user):
     print(user)
    # print(user["age"])
    # print(user["age"])



#save_users(id=1, name="Marc", age=30)





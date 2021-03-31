# 1. Create a function called greetings that takes one argument as string and returns the name

#def greeting(name):
#    return "Welcome " + name

#print(greeting("Jose"))

# 2. Declare a list of numbers from 1 - 9.
# Iterate through the list and print the list
# declare, list, iterate, print
#numList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#for item in numList:
#    print(item)

# 3. Write boolean operators
# If a == b and c == d print true
# write an example of the boolean operators

#if "a" == "b" and "c" == "d":
#    print(True)

# 4. Create a list of five numbers, starting from zero

#numbers = [0, 1, 2, 3, 4]

#for num in range(5):
#    numbers.append(num)

# Create a tuple with the same information

#tuple_number = (0, 1, 2, 3, 4)
#numbers_tuple = tuple(numbers)
#print(tuple_number)
#print(numbers_tuple)

# Change the value fot the tuple in the last index

# CAN NOT CHANGE A TUPLE
# BECAUSE TUPLES ARE IMMUTABLE
# UNLIKE LISTS, THAT CAN BE CHANGED AS THEY ARE MUTABLE

# 5. Create a dictionary with 2 key pairs
# first key is 'name' and the value of the name is James
# second key is 'age', and the value is an int 18
# print tha values of keys

#my_dictionary = {
#    "name": "James",
#    "age": 18
#}

#print(my_dictionary["name"])
#print(my_dictionary["age"])

# 6. Create a class called Jose and initialise the class that takes two arguments
# create an object of that class

#class Jose:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age

#person = Jose("Jose", 24)
#print(person.name)
#print(person.age)

# Create another object from the same class, called student
# print the attributes

#student = Jose("James", 99)
#print(student.name)
#print(student.age)

# 7. Write the correct syntax to create a set
#setA = {1, 2, 3, 4}
# write difference between sets and all other collectons
# answer: unordered
#print(setA)

#setA.update({5})
#print(setA)
#setA.add(10)
#print(setA)

# 8. Create a method that takes one argument as a string(my name)
# if the name == "Jose" return true, else return false

#def is_jose(name):
#    if name == "Jose":
#        return True
#    else:
#        return False

#print(is_jose("Jose"))
#print(is_jose("James"))

# 9. Create a class called human with one method called breathe that returns breathing
# Create another class called student that inherits from human and create object of student class
# and call the function from the parent class

#class Human:
#    def __init__(self):
#        self.alive = True

#    def breathe(self):
#        return "breathing"

#class Student(Human):
#    pass

#student = Student()
#print(student.breathe())

# 10. Write the correct syntax to use the keyword super
#class Human:
#    def __init__(self):
#        self.alive = True

#    def breathe(self):
#        return "breathing"

#class Student(Human):
#    def __init__(self):
#        super().__init__() # Super refers to the parent class of a class, when used in this manner you can use methods of the parent class such as the __init__ to affect the child

#student = Student()
#print(student.breathe())

# 11.
# Create a variable called user_data and store 0 to 4 in that list
# Create a function that makes an argument as a list
# The function return True if the datatype is list, False otherwise

#user_data = [0, 1, 2, 3, 4]
#user = 1

#def is_list(the_list):
#    if type(the_list) == list:
#        return True
#    else:
#        return False

#print(is_list(user_data))
#print(is_list(user))

# 12.
# Create a function called get_percentage
# Takes two integers as arguments
# Returns the percentage of two

#def get_percentage(num1, num2):
#    percentage_num1 = (num1 / (num1 + num2)) * 100
#    return percentage_num1

#print(get_percentage(10, 90))

# 13.
# Create a function
# Takes 2 arguments as int
# Divide first val by second val
# Returns the outcome
# Check if the numbers given is divisible by o.
# Through an error if it can not be divided by 0 else the value

#def divide(num1, num2):
#    try:
#        return int(num1) / int(num2)
#    except ZeroDivisionError as error:
#        return error

#print(divide(9, 0))

# 14.
# Write five odd numbers in a list and then five even numbers in another list
# Iterate through these lists to combine and display the numbers in a method

#odd_numbers = [1, 3, 5, 7, 9]
#even_numbers = [2, 4, 6, 8, 10]

#list1 = [1, 3, 5, 7, 9]

#list2 = [2, 4, 6, 8, 10]

#both = []

#def combined(odds, evens):
#    for odd, even in zip(odds, evens):
#        both.append(odd)
#        both.append(even)

#    return both

#print(combined(list1, list2))

#def combine_odd_even(odd_list, even_list):
#    new_list = odd_list
#    count = 1
#    for n in even_list:
#        new_list.insert(count, n)
#        count += 2

#    print(new_list)

#odd_nums = [1, 3, 5, 7, 9]
#even_nums = [0, 2, 4, 6, 8]
#num_list = []

#def odd_even(odd_nums, even_nums, num_list):
#    for x in range(5):
#        num_list.append(even_nums[x])
#        num_list.append(odd_nums[x])
#    print(num_list)

#odd_even(odd_nums, even_nums, num_list)

# 15.
# Create a dictionary called shopping_list with 3 key value pairs.
# Milk: 1, yogurt: 1.10, ice cream: 2.5
# Create a function that takes an arg as the dictionary. Iterate through the values of dictionary and add the total value and return the total cost

#shopping_list = {
#    "milk": 1,
#    "yogurt": 1.50,
#    "ice cream": 2.5
#}

#def total_cost(dictionary):
#    amount = 0
#    for item in dictionary.values():
#        amount += item
#    return amount

#print(total_cost(shopping_list))

# 16.
# Create a dictionary called shopping_list with 3 key value pairs.
# Milk: 1, yogurt: 1.10, ice cream: 2.5
# Get the cost of the yogurt.

#shopping_list = {
#    "milk": 1,
#    "yogurt": 1.50,
#    "ice cream": 2.5
#}

#print(shopping_list["yogurt"])

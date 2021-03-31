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

class Human:
    def __init__(self):
        self.alive = True

    def breathe(self):
        return "breathing"

class Student(Human):
    pass

student = Student()
print(student.breathe())

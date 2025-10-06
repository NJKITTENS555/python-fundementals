# USER IMPUT IN PYTHON
import random

print("\n----User Input Demonstration------")

name = input("enter your name: ")
print("hello", name)

age = int(input("Enter your age: "))
print(type(age))

age_number = int(age)
print("Next year, you will be:", age_number + 1)
print(type(age_number))

# Example with float imput
height = input("Enter your height in meters: ")
print("You are", height, "meters tall.")


color = input("Enter your favorite color: ")
print("what is your favorite color", color)

one = input("type one number: ")
two = input("type 2nd number: ")
sum = one + two 
print(sum)


side = input(" how many sides do you want this dice to have: ")
sides = random.randint(0 , side)
print("dice with", side, "sides. rolled number:" , sides)

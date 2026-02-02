#python functions are blocks of code that can be reused

# to run a function you "call" the function by writing its name"

print("Funtions (procedgers)")

print("\n Example 1")

def say_hi():
    print("Hi")

def say_bye():
    print("bye")

say_hi()
say_bye()


def express_this(e):
    return e 

expression = express_this(1 + 2) 
print(expression)
expression = express_this(45 * 6)
print(expression) 

def greeter(n): #n is the parameter
    return f"HI {n}!"

first = greeter("kludzy")
second = greeter("frederick foz")
third = greeter("Gary")

print(first, second, third) 



print("\n Example 4")

def remainder(a,b):
    return a%b 
result = remainder(3,2)
print("Remainder:", result)


def is_far(distance):
   #insert BASE CASE
    if distance < 1:
        return "error"
   
    if distance  >= 100:
        return "Thats far!"
    elif distance < 100 and distance > 20:
        return "Thats not too far!"
    elif distance < 20:
        return "Thats nearby!"



print(is_far(50))

# I want to create a function that takes in a number and doubles it, then adds it to a list.
# The function should also take in a number of times that we should double the number

def double_sequencer(number, times):
    value = number
    sequence = []

    for i in range(times):
        value = value * 2
        sequence.append(value)

    return sequence

result = double_sequencer(1, 5)
print(result)

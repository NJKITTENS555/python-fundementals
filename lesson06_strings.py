# Basic string creation and indexes:
greeting = "Hello"
name = "Ada"
print(greeting, name)

# 0 1 2 3 4 
# H e l l o
second_letter = greeting[1]
print(second_letter)

message = greeting + " " + name + "!!!!"
print("Concatenated message:", message)

word = "Super-cali-fragil-istic-expi-ali-docious"
print("First letter:", word[0])
print("Last letter:", word[-1])
print("letter : ", word[-13])
print( word[0:5])
print(word[-7:])
print(word[::2])

print(word[::-1])
print("Reversed, stepping every third letter:", word[::-3])
country = "portogal"
length_of_word = len(country)
print(length_of_word)

phrase = "SpoNgEbOb"
print("\nUppercase:", phrase)
print("\nlowercase:", phrase)
print("Capitalized first letter:", phrase.capitalize())
print("Title Format:", phrase.title())


#Find and replace text
sentence = "I'm a goofy goober"
new_sentence = sentence.replace("I'm", "You're")
new_replacment = sentence.replace("goofy", "goober")
print(sentence)
print(new_sentence)
print(new_replacment)

name = "Ada"
age = 28
city = "london"

print(f"Hello, my name is {name}. I am {age} yeras old and live in {city}.")
# f strings can do math inside {}

print(f"next year I will be {age + 1}. My name in uppercase is {name.upper()}")

# Challenge 1: Favorite Quote
# Ask the user for their favorite quote and display its length.
# EXAMPLE OUTPUT:
# Enter your favorite quote: Those who believe in telekinetics, raise my hand.
# Your quote is 48 characters long.

Favorite_quote = input("What is your favorite quote?: ")
print( f"quote is {len(Favorite_quote)} charicters long")

firstname = input("what is your first name:")
lastname = input("what is your last name:")
print(f"{lastname}, {firstname}")


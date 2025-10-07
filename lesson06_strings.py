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


# LOOPS IN PYTHON
# Loops repeat a block of code until they hit a limit or condition.
# They exist to save us from typing the same line 500 times.
# Python gives us for-loops and while-loops.
# 
print()
print("--- Loops in Python ---")

# The for-loop.
# A for-loop repeats for each element in a sequence (like a list or string).
import time 
#animals = ["lamb", "sheep", "cow", "goose", "donkey" ]

#print("\nOur animals:", animals)
#print("\n--- For Loop: visiting each animal ---")

#for animal in animals:
#    print("Now petting a", animal)
#    time.sleep(1.5)

 #   if animal =="sheep":
  #      print("hi shep!!")
# print("Now I have pet all the animals!")

#for i in range(5):
 #   print("counting:", i)

# range(start, stop, step)
#print()
print("----range() with start, stop, step ----")

print("--- Iterating over strings ---\n")

fav_word = "Shenanigan"

for letter in fav_word:
    print(letter)
print("--- Iterating over strings ---\n")

fav_word = "Shenanigan"

for letter in fav_word:
    print(letter, end = " ")
    fav_word = "Shenanigan"
letter_list = []

for letter in fav_word:
    print(letter, end="")
   # letter.append(letter_list)
    print(letter_list)

print()

# ---------------------------------------------------------
# WHILE LOOPS
# ---------------------------------------------------------
# A while-loop repeats *while* a condition is true.
# If you forget to change the condition, it loops forever.
# And then your program becomes immortal. Avoid that.

# += to add to a variable, -= to subtract to a variable, = to overright 
import time
count = 0

#while count < 5:
 #   print(f"Loopin'. We are on loop # {count}.")
  #  count += 1
   # time.sleep(0.5)

#print("We have escaped loop!!")
#user_input = ""

#while user_input == "exit":
#    user_input =  input("type 'exit' to escape :") 
 #   user_input = ""

count = 60
increment = 1

while count > 0:
    if count < 0: 
        break
    count -= increment
    increment += 1
    print(count)


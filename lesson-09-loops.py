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
animals = ["lamb", "sheep", "cow", "goose", "donkey" ]

print("\nOur animals:", animals)
print("\n--- For Loop: visiting each animal ---")

for animal in animals:
    print("Now petting a", animal)
    time.sleep(1.5)

    if animal =="sheep":
        print("hi shep!!")
print("Now I have pet all the animals!")

for i in range(5):
    print("counting:", i)

# range(start, stop, step)
print()
print("----range() with start, stop, step ----")
# LISTS IN PYTHON
# Lists store multiple values in one variable.
# They are ordered, mutable (changeable), and allow duplicates.
print()
print("--- Lists in Python ---")

animals = ["donkey", "pangolin", "blobfish"]
numbers = [2, 4, 6, 8, 10]
mixed = ["piffle", 42, True, 9.99]

print(animals)
print(numbers)
print(mixed)

print("--- Indexing: how to access the elements of a list ---")
print("First Element:,", animals[0])
print("Second element:", animals[1])
print("Last element:", animals[-1])

print()
print("--- Modifying Lists ---")

print("--- Modifying Lists ---")
animals[0] = "babirusa"
print(animals)

animals.append("glass frog")
print(animals)

# insert element at specific index

animals.insert(3, "aye-aye")
print("Inserted one animal:", animals)
animals.insert(1, "camel")
print("Inserted another animal:", animals)

print(animals.remove("camel"))

last_animal = animals.pop()
print("Removed animal:", last_animal)
print("Remaining animals:", animals)

print()
print("--- Useful List Functions ---")

nums = [3, 7, 1, 9, 4, 2, 5, 8, 6, 0]
print("Original Numbers:", nums)
print("Length of the list:", len(nums))
print("Min:", min(nums))
print("Max:", max(nums))
print("Sum:", sum(nums))

nums.sort()
print(nums)

animals.sort
print(animals)
nums.reverse()
print(nums)

print()
print("--- Checking Membership ---")

if "cat" in animals:
    print("Cat is in the list!")
else:
    print("Cat is not in the list.")

print()
print("--- Copying Lists ---")

newlist = [1, 2, 3]
copiedlist = newlist.copy()
copiedlist.append(4)
print(newlist)
print(copiedlist)

matrix = [  
    [1,2,3], 
    [4,5,6], 
    [7,8,9]  
    ] 

print(matrix[2][2])

list123 = [1, 2, 3, 4, 5, 6]
print(list123)
listnum = input("type a number:")
newlist123 = [1, 2, listnum, 4, 5, 6]
print(newlist123)

shopping = []
shopping.append("nuclear waste")
shopping.append("the tsar bomb")
shopping.append("landmines")
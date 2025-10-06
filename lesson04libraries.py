# python libraies are repositories of code 
import math 
print("/n ---math Library---", math.sqrt(25))
print("Square root:", math.sqrt(25))

print("round up: ", math.ceil(4.2)) 
print("round down: ", math.floor(4.2))
print("power: ", math.pow(2, 5))
print("Pi:", math.pi)

#-----------------
#-RANDOM-LIBRARY--
#-----------------

seed = 76456 #6 digets
tie = seed * 5
rand = tie * 11
random12 = math.floor(rand / 100)
print( random12 )

seed1 = 197.12
step1 = seed1 / 6.7
step2 = step1 - 800
step3 = step2 * 737063
result = math.floor(step3)
limitednumber = step3 - result
answer = math.floor(limitednumber * 10)
print(answer)



import random 
# methods:
print("Random integer: ", random.randint(0, 1))
print(random.random)
mylist = ["egg" , "chicken", "ham", "turkey", ]
random.choice(mylist)

radius = 14
circle_area = 3.14
#print( circle_area * radius**)   

dieroll = ["1", "2", "3", "4", "5", "6" ]
print(random.choice(dieroll))
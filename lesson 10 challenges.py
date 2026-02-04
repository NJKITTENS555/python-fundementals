# PROCEDER calculator(a,b):
#   print(a+b)
#   print(a-b)
#   print(a*b)
#   print(a/b)
# a <--- number
# b <--- number

def calculator(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

calculator(12,3)




# proceder average(a,b,c):
#   d = (a+b+c)/3
#   return(d)
#
# a <--- number
# b <--- number
# c <--- number
#
# print


def average(a,b,c):
    return (a+b+c)/3

jef = average(1,2,3)
print(jef)


# proceder is_even(e)
#   if (e % 2 = 0)
#       return(Its Even!!)
#   else
#       return(Its odd!!)

def is_even(e):
    if e % 2 == 0:
        return "Its Even!"
    else:
        return "Its Odd!"

joe = is_even(627831)
print(joe)
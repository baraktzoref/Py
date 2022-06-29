import random

x1 = random.randint(0,1000)
x2 = random.randint(0,1000)

if x1 > x2:
    print("The first number {} is bigger than the second number {}".format (x1,x2))
elif x2 > x1:
    print("The second number {} is bigger than the first number {}".format (x2,x1))
else:
    print("Both numbers are equal {} {}".format (x1,x2))
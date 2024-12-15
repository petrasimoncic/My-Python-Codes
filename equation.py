import random

x = random.randint(0,100)
print("Random number:", x)

y = int(input("Enter the correct value for y, so that the random number + y adds up to the next multiple of 10: "))

if 0 < y <= 10 and (x + y) % 10 == 0:
    print("Correct")
else:
    print("Inccorect")
#Finding random numbers
import random
print("Welcome  to Dice rolling stimulator")

x="yes"
while x== "yes":
    num = random.randint(1, 6)

    # Making Dice
    if num == 1:
        print("------------")
        print("|          |")
        print("|     0    |")
        print("|          |")
        print("------------")

    if num == 2:
        print("------------")
        print("|          |")
        print("|  0    0  |")
        print("|          |")
        print("------------")

    if num == 3:
        print("------------")
        print("|     0    |")
        print("|     0    |")
        print("|     0    |")
        print("------------")

    if num == 4:
        print("------------")
        print("|  0    0  |")
        print("|          |")
        print("|  0    0  |")
        print("------------")

    if num == 5:
        print("------------")
        print("|  0    0  |")
        print("|     0    |")
        print("|  0    0  |")
        print("------------")
    if num == 6:
        print("------------")
        print("|  0    0  |")
        print("|  0    0  |")
        print("|  0    0  |")
        print("------------")
    x = input(" Wanna run the Dice again :yes or no?")





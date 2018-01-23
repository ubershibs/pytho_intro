from random import randint

print("Welcome to Dice Roll")

response = "y"
while response == "y":
    print("You rolled a " + str(randint(1,6)))
    response = input("Would you like to roll the dice again? y/n: ")
else:
    print("Bye!")

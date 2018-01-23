from random import randint

print("Welcome to the Random Number Game")
print("I've picked a number from 1 to 20. If you can guess it, you win!")

guess = 0
solution = randint(1, 20)

def get_guess():
    guess = input("What's your guess? ")
    while not guess.isdigit():
        print("Your guess was not a digit.")
        guess = input("Try again: ")
    return int(guess)

while guess != solution:
    guess = get_guess()
    if guess < solution:
        print("Your guess is too low! Try again!")
    elif guess > solution:
        print("Your guess is too high! Try again!")
else:
    print("Right on, you got it!")

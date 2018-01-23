from random import randint

dictionary = ["apple", "banana", "orange", "avocado", "clementine"]

print("Welcome to Hangman!")
word = list(dictionary[randint(0, len(dictionary) - 1)])
misses = 0
status = list("_" * (len(word)))
guesses = []
print("Your word has " + str(len(word)) + " letters")

while misses < 4:
    print(" ".join(status))
    guess = input("Guess a letter: ")
    while len(guess) > 1 or not guess.isalpha():
        guess = input("Guess a SINGLE letter: ")
    else:
        # Add duplicate guess check here
        if guess.lower() in word:
            for i in range(0, len(word)):
                if word[i] == guess.lower():
                    status[i] = guess.lower()
                i += 1
        else:
            misses += 1
            print("You missed! That's " + str(misses) + " of 4 misses!")
    if status == word:
        print("".join(status))
        print("Congrats! You got it!")
        break
else:
    print("Sorry, you are out of turns!")

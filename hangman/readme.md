# Hangman
A quick game of Hangman I came up with, while working through [these projects from the Knight Lab](https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/). The game picks a random work from the list called 'dictionary', and then asks you to guess a letter. If you input more than one letter or anything other than a letter, you'll be asked to guess again. If your guess is in the word, the status will be updated. If your guess is not in the word, you'll register a miss. You lose after 4 misses, and win if you get the word.

Updates:
* Added ability to accept both upper and lower case letters.
* Added check for duplicate guesses ("You already guessed that letter.")

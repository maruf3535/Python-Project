# Python Exercise 3 - Guess The Number


# Guess the number in 5 chances. if user fail to guess the number in limited chances, user will be game over. If user can able to guess the number in limited chances, then congrate to the user and show the used the number of chance/chances.

# https://www.w3schools.com/python/ref_random_randint.asp # Next 3 line codes was taken from this link.
"""
import random
print(random.randint(0, 25))
#returns a number between 3 and 9 (both included)
"""

import random as r
from time import sleep
number = r.randint(0, 25)
# number = 15
chance = 5
print("Guess the number: (0 - 25)\n                 CHANCE: ", chance)
i = 0
while (i < 5):
    guessNum = int(input())
    i += 1
    chance -= 1
    if i == 5:
        if guessNum == number:
            print("Congratulation! You won the game and you used", i, "chances")
            break
        elif i == 5:
            print("The answer is", number)
            break
    elif guessNum < number:
        print("Please try again!")
        print("You should increase the input number.")
    elif guessNum > number:
        print("Please try again!")
        print("You should decrease the input number.")
    elif guessNum == number:
        print("Congratulation! You won the game and you used", i, "chances")
        break
    if guessNum != number:
        print("                 CHANCE: ", chance)

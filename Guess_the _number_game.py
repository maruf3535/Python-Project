# Guess The Number Game

import random as r
from time import sleep
number = r.randint(0, 25)
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

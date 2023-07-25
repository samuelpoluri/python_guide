# importing random module
import random


# defining a class object as Dice
class Dice:

    # defining roll function
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        # printing the numbers from 1-6 at random
        return first, second


dice = Dice()
print(dice.roll())

"""This is a Number Guessing game which takes a range of numbers specified by the user. It stores a number from the specified range at random and asks the user to guess the number."""
import random
# takes a range of numbers from zero to user specified (ex: 10, the program takes from 0 to 10 numbers.)
number = input("Please enter the range of numbers: ")

if number.isdigit():
    number = int(number)
    if number <= 0:
        print("Please enter the number larger then 0")
        quit()
else:
    print("Enter a valid number")
    quit()

# the program selecting a number at random from the given range of numbers. 
random_number = random.randint(0, number)
guess_count = 0

while True:
    guess_count += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Type a number")
        continue

    if user_guess == random_number:
        print("You got it right!")
        break
    elif user_guess > random_number:
        print("You are above the number")
    else:
        print("You are below the number")
print(f"You got it in {guess_count} guesses!")

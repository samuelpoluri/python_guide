import random
number = input("Please enter the range of numbers: ")

if number.isdigit():
    number = int(number)
    if number <= 0:
        print("Please enter the number larger then 0")
        quit()
else:
    print("Enter a valid number")
    quit()

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

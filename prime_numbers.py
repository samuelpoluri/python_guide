# Enter a number to check if it is a prime or not
num = int(input("Enter a number: "))
# Set flag variable to False
flag = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num):
        # applying formula (num % i) to check for factors
        if (num % i) == 0:
            flag = True
            break

    # if flag is True
    if flag:
        print(num, "is not a prime number.")
    else:
        print(num, "is a prime number.")

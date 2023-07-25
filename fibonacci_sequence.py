# Enter the number of fibonacci numbers to be displayed
number_of_terms = int(input("Enter the number of terms: "))

# assigning n1 and n2
n1 = 0
n2 = 1
count = 0

# number of terms cannot be negative
if number_of_terms <= 0:
    print("Please enter positive numbers.")
elif number_of_terms == 1:
    print(n1)
# displaying fibonacci sequence1
else:
    while count < number_of_terms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

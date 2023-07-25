# Checking whether a triangle is possible with positive area given 3 angles.
# prompting the user to give the three angles
def is_triangle_possible():

    a = int(input("Enter the first angle: "))
    b = int(input("Enter the second angle: "))
    c = int(input("Enter the third angle: "))

    # any angle must not equal to "Zero"
    # checking whether the sum of the given angles is 180
    if a != 0 and b != 0 and c != 0 and a+b+c == 180:
        if (a+b) >= c or (b+c) >= a or (a+c) >= b:
            print("The triangle with positive area is possible.")
        else:
            print("The triangle with positive area is not possible.")
    else:
        print("The triangle with positive area is not possible\n"
              "Reason: The sum of all the angles does not equal to 180.")


is_triangle_possible()

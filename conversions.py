# Python program to convert units
# prompting the user to specify the conversion type
prompt = input("What do you want to convert (W)eight or (D)istance)? ")


# defining weight function
def weight():
    unit = input("select your input unit (L)bs or (K)g: ")
    weight = float(input("Weight: "))
    if unit.upper() != "K":
        converted = weight * 0.45
        print("Weight in Kg is:", converted)
    else:
        converted = weight / 0.45
        print("Weight in Pounds is:", converted)


# defining distance function
def distance():
    unit = input("Select your input unit (M)eters or (F)eet? ")
    distance = float(input("Distance: "))
    if unit.upper() != "F":
        converted = distance * 3.28084
        print("Distance in Feet is:", converted)
    else:
        converted = distance / 3.28084
        print("Distance in Meters is:", converted)


if prompt == "w":
    weight()
elif prompt == "d":
    distance()
else:
    pass

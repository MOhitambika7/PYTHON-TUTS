# Python weight converter.
weight = float(input("Enter the weight: "))
unit = input("Kilograms or pounds? (K/L) : ")
if unit == "K":
    newWeight = weight * 2.205
    print(f"The weight is:- {newWeight} lbs")
elif unit == "L":
    newWeight = weight/2.205
    print(f"The weight is:- {newWeight} kgs")
else:
    print(f"You entered the invalid unit {unit}. Only accepts K and L.")        
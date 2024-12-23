unit = input("Enter the unit for the temperature:- (K/F):-  ")
Temp = float(input("Enter the temperature:- "))
if unit == "K":
    newTemp = round((9 * Temp)/(5+32), 3)
    print(f"The temperature in farenheit scale is:- {newTemp} deg. F")
elif unit == "F":
    newTemp = round((Temp - 32 ) * (5/9), 3)    
    print(f"The temperature in celcieus scale is:- {newTemp} ")
else:
    print(f"{unit} is invalid unit for the temperature.")    
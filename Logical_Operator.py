# Uses of the logical operatores in python programming language.(i.e.:- or, and, not.)



Temp = float(input("Enter the temperature in degree centigrade:- "))
isRaining = bool(input("Enter the condition True or False:- "))
if Temp < 35 and Temp > 10 or isRaining == False:
    print("The outdoor event is scheduled as mentioned in event card.")
elif Temp > 35 and Temp < 10 or isRaining == True:
    print("The outdoor event is cancelled and is postponded until the publication of the next notice.")
elif Temp < 35 and Temp > 10 or isRaining == True:
    print("The out door event is cancelled due to raining and is postponded until the publication of the next notice")
else:
    print("Enter the valid data.")          
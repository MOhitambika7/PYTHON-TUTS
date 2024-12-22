age = int(input("What is your age? :- "))
if age >= 18:
    print("Eligible to drive a car. Can get a trial and have a license.")
elif age < 18:
    print("Not eligible to drive a car and to get a license.")
else:
    print("Invalid input. Please fill the valid age.")
    
response = input("Would you like to eat food? (Y/N):- ")
if response == "Y":
    inpt = str(input("Food:- "))
    print(f"I want to eat {inpt} ")
else:
    print("I am not hungry now. Thanks for askiing.")  
    
Online = True
if Online:
    print("The user is online.")
else:
    print("Currently user is offline.")          
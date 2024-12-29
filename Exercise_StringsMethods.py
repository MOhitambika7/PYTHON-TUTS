# Validate user input exercise.
# User name no more than 12 character.
# Username must not contain any spaces.
# Username must not contain digits.

username = input("Enter yuor username:- ")
if len(username) > 12:
    print("Length of the username ie too long. Enter username having characters less tha 12.")
    
elif not username.find(" ") == -1:
    print("Your Username should not contain any spaces.")

elif not username.isalpha():
    print("Username must not contain any digits.")
            
else:
    print(f"Welcome {username}")    
    
#Use of the negetive index starts from last(i.e -1 ----> last digit.)    
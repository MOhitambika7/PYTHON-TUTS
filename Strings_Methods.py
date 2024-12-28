# STRINGS METHODS:-
STRINGS = input("Enter your string:- ")

Result = len(STRINGS) #Gives the length of the character(i.e number of characters including spaces.)
print(Result)
Result = STRINGS.find("") # Finding the occurence of the space between any sstrings.
print(Result)
# While finding the occurences of the characters or any spaces and symbols in string the procedure of finding the occurence always starts from the 0 position of the first character.

Result = STRINGS.capitalize()
print(Result)

Result = STRINGS.isdigit()
print(Result)
Result = STRINGS.isalpha()
print(Result)

phone_number = input("Enter the phone number:- ")
result = phone_number.count("-")
print(result)



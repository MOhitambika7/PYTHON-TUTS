# input() ----> A function that promts the user to input the data returns the entered data.
name = input("What is your name?:  ")
print(f"My name is {name}.")

age = input("How old are you?: ")
age = int(age) #After taking user input, We have to typeast the age variable to int.
age = age + 1
print(f"I am {age} years old.")

#In the above typecasting this method seems to take the extra lines in the code so we have anotyher approach and that is:-

Age = int(input("How old are you?: "))
Age = Age + 1
print(f"I am {Age} years old.")
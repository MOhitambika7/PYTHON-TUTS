#TypeCasting ----> Process to convert a variable from one datatype to another str(), int(), float(), bool()

name = "Zen"
age = 14
GPA = 3.15
isStudent = True
print(type(name))
print(type(age))
print(type(GPA))
print(type(isStudent ))

GPA = int(GPA) #Here in this portion we Truncate the decimal portion.
print(GPA)

age = str(age)
print(age)
print(type(age))
age += "1"
print(age)

name = bool(name)
print(name)

Name = ""
Name = bool(Name)
print(Name)
#The type casting of checks either some one entered nae or not. If there is name it returns true but if there is no name entered it reuturns false.
#Tyoe casting is mainly used to handle user input.
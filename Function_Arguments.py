#Positional arguments.

def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")
    
greet("Alice", 10)  #Positional Arguments.

greet(age = 10, name = "Bob") #Keyword Arguments.

def details(Name, Age = 11):
    print(f"Hello {Name}, you are {Age} years old.")

details("Alice") #Uses the default value of 18.
details("Mady", 14)#Overrides the default values.
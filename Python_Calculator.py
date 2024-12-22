#Python Calculator.
Operator = input("Enter the operator:- +, -, *, /")
num1 = float(input("Enter the  first number :- "))
num2 = float(input("Enter the second number :- "))
if Operator == "+":
    result = num1 + num2
    print(result)
elif Operator == "-":
    result = num1 - num2
    print(result)   
elif Operator == "*":
    result = num1 * num2
elif Operator == "/":
    result = num1 / num2

else:
    print("Invalid selection of the operator")             
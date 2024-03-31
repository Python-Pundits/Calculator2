operator = input("Enter an operator: + - * / " )

num1 = float(input("Enter First Number:" ))

num2 = float(input("Enter Second Number:" ))

if operator == "+":
    addition = num1 + num2
    print(round(addition))
    
elif operator == "-":
    substraction = num1 - num2
    print(round(substraction))
    
elif operator == "*":
    multiplication = num1 * num2
    print(round(multiplication))
    
elif operator == "/":
    division = num1/num2
    print(round(division))
    
else:
    print(f"{operator} is an invalid operator")
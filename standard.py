#Changes made: I defined a function called "standard()" so that it can be called upon in the "main.py" file
exit = True

def standard():
    operator = input("Enter an operator: + - * / " )

    num1 = float(input("Enter First Number:" ))

    num2 = float(input("Enter Second Number:" ))
    
    if operator == "+":
        addition = num1 + num2
        print(round(addition))
    
    elif operator == "-":
        substraction = num1 - num2
        print(substraction)
    
    elif operator == "*":
        multiplication = num1 * num2
        print(multiplication)
    
    elif operator == "/":
        division = num1/num2
        print(division)
    
    else:
        print(f"{operator} is an invalid operator")
        
while exit ==True:
    standard()
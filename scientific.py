import math

# functions
def sin(a):
    return math.sin(a)

def log(a):
    return math.log(a)

def tan(a):
    return math.tan(a)

def cos(a):
    return math.cos(a)

def sqrt(a):
    return math.sqrt(a)

exit = True

# user input
def operate():
    operation = input("Select operation [sin, log, tan, cos, sqrt, exit]: ")
    number = int(input("Input number: "))

    if operation == "sin":
        result = sin(number)
    elif operation == "log":
        result = log(number)
    elif operation == "tan":
        result = tan(number)
    elif operation == "cos":
        result = cos(number)
    elif operation == "sqrt":
        result = sqrt(number)
    elif operation == "exit":
        quit()
        #Changes made below:
    else:
        print(f"{operation} is an invalid operator ")
        print("==================")

    # output
    print(f"Answer = {result}")

# app re-render
while exit == True:
    operate()


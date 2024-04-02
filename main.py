# from standard import standard()
from scientific import operate
from binary import num_conv

print("/\/\/\/ CALCULATOR \/\/\/")
print("Modes:")
print("1. Standard")
print("2. Scientific")
print("3. Binary")

user_mode = int(input("Select Mode: "))

# if user_mode == "1":
#     standard_calc()

if user_mode == "2":
    operate()

if user_mode == "3":
    num_conv()

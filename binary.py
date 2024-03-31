print("Choose Conversion")
print("=======================")
print(" ")
print("1: Decimal to Binary")
print("2: Decimal to Octal")
print("3: Decimal to Hexadecimal")
print("4: Binary to Decimal")
print("5: Binary to Octal")
print("6: Binary to Hexadecimal")
print("7: Octal to Decimal")
print("8: Octal to Binary")
print("9: Octal to Hexadecimal")
print("10: Hexadecimal to Decimal")
print("11: Hexadecimal to Binary")
print("12: Hexadecimal to Octal")
print("13: Exit")
print(" ")
print("=======================")

exit = True
choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]

def num_conv():
    choice = str(input("Select an option: "))
    
    if choice not in choices:
        print("Select ONLY from the options given above!")
        
    if choice == "1":
        decimal = int(input("Enter your Decimal Value:  "))
        convert = bin(decimal)
        print (convert)
        
    if choice =="2":
        decimal = int(input("Enter your Decimal value:  "))
        convert = oct(decimal)
        print(convert)
        
    if choice == "3":
        decimal = int(input("Enter your Decimal value:  "))
        convert = hex(decimal)
        print (convert)   
        
    if choice == "4":
        binary = int(input("Enter your Binary value:  "))  
        convert = int(str(binary), 2)
        print (convert)                     
    if choice =="13":
        exit = False
        quit()
        
while exit == True:
        num_conv()
        

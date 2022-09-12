# Alex Gray
# Input, output, else, elif, if

# provide instruction to the user
# prompt user for input

print("select the operation to perform: ")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()

if operation == "1":
    # code for add
    num1 = input("Enter first number: ")
    num2 = input("Enter seconf number: ")
    print("The sum of your equation is " + str(int(num1) + int(num2)) + ".")
    
elif operation == "2":
    # code for subtract
    num1 = input("Enter first number: ")
    num2 = input("Enter seconf number: ")
    print("The answer to your equation is " + str(int(num1) - int(num2)) + ".")
    
elif operation == "3":
    # code for multiply
    num1 = input("Enter first number: ")
    num2 = input("Enter seconf number: ")
    print("The answer to your equation is " + str(int(num1) * int(num2)) + ".")
    
elif operation == "4":
    # code for divide
    num1 = input("Enter first number: ")
    num2 = input("Enter seconf number: ")
    print("The answer to your equation is " + str(int(num1) / int(num2)) + ".")

else:
    print("Invalid Entry. Please Enter A Number From 1-4.")
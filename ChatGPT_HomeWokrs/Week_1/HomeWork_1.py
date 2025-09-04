first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
operation = input("Enter the operation +, -, *, / : ")
if operation == "+":
    print("Result:", first_number + second_number)
elif operation == "-":
    print("Result:", first_number - second_number)
elif operation == "*":
    print("Result:", first_number * second_number)
elif operation == "/":
    print("Result:", first_number / second_number)
else:
    print("You entered wrong operation")
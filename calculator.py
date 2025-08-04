num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
arithmetic_operation = input("Enter a mathematical operation(+, -, *, /): ")


if arithmetic_operation == "+":
    value = num1 + num2
    print(f"{num1} + {num2} = {value}")
elif arithmetic_operation == "-":
    value = num1 - num2
    print(f"{num1} - {num2} = {value}")
elif arithmetic_operation == "*":
    value = num1 * num2
    print(f"{num1} * {num2} = {value}")
elif arithmetic_operation == "/":
    if num2 != 0:
        value = num1 / num2
        print(f"{num1} / {num2} = {value}")
    else:
        print("Error, division by zero is not allowed!")
else:
    print("Invalid operation! Please use +, -, *, or /.")
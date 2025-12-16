num1 = float(input("First number: "))
operation = input("Operation: ")
num2 = float(input("Second number: "))


if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/' and num2 != 0: 
    result = num1 / num2
else:
    result = "Invalid operation or division by zero"


print(f"{num1} {operation} {num2} = {result}")
operator = input("Enter operator: (+ - * /) ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == '+':
    result = num1 + num2
    print(f'The result is {result}')
elif operator == '-':
    result = num1 - num2
    print(f'The result is {result}')
elif operator == '*':
    result = num1 * num2
    print(f'The result is {result}')
elif operator == '/':
    result = num1 / num2
    print(f'The result is {result}')

else:
    print(f'{operator} is Invalid operator')

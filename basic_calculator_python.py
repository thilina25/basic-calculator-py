operation = ["+", "-", "*", "/"]

while True:
    user_input = input("Enter a mathematical expression: + - * / ")

    if user_input in operation:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == "+":
            print(f"Result{num1 + num2}")

        elif operation == "-":
            print(f"Result{num1 - num2}")

        elif operation == "*":
            print(f"Result{num1 * num2}")

        elif operation == "/":
            if operation == 0:
                print("Error! Division by zero")

            else:
                print(f"Result{num1 / num2}")

        break
    else:
        print("Invalid operation")

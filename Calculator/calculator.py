print("==========================")
print("    SIMPLE CALCULATOR")
print("==========================")

again = "y"

while again.lower() == "y":

    # Get user input
    num1 = float(input("\nEnter first number: "))
    operator = input("Enter (+, -, *, /, %, **): ")
    num2 = float(input("Enter second number: "))

    # Perform calculation
    if operator == "+":
        result = num1 + num2
        print("Answer:", result)

    elif operator == "-":
        result = num1 - num2
        print("Answer:", result)

    elif operator == "*":
        result = num1 * num2
        print("Answer:", result)

    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
            print("Answer:", result)
        else:
            print("Error: Cannot divide by zero!")

    elif operator == "%":
        if num2 != 0:
            result = num1 % num2
            print("Answer:", result)
        else:
            print("Error: Cannot divide by zero!")

    elif operator == "**":
        result = num1 ** num2
        print("Answer:", result)

    else:
        print("Invalid operator!")

    # Ask user if they want to continue
    again = input("\nDo another calculation? (y/n): ")

print("\nThanks for using my calculator!")
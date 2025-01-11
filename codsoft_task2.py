def calculator():
    print("Welcome to the Simple Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Get user input for operation
    choice = input("Enter the number corresponding to the operation (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        try:
            # Get user input for numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Perform the chosen operation
            if choice == '1':
                result = num1 + num2
                operation = "+"
            elif choice == '2':
                result = num1 - num2
                operation = "-"
            elif choice == '3':
                result = num1 * num2
                operation = "*"
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    return
                result = num1 / num2
                operation = "/"

            # Display the result
            print(f"Result: {num1} {operation} {num2} = {result}")
        except ValueError:
            print("Error: Invalid input. Please enter numeric values.")
    else:
        print("Invalid operation choice. Please select from 1, 2, 3, or 4.")

# Run the calculator
calculator()


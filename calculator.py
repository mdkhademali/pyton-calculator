# Calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def get_float_input(prompt):
    """Helper function to handle invalid inputs when getting numbers."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Main program loop
while True:
    print("\nChoose an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    choice = input("What operation would you like to perform? (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = get_float_input("Enter the first number: ")
        num2 = get_float_input("Enter the second number: ")

        # Perform the chosen operation and display the result
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input! Please choose a valid operation.")

    # Ask if the user wants to perform another calculation
    again = input("\nWould you like to perform another calculation? (yes/no): ").lower()
    if again != 'yes':
        print("Thank you for using the calculator!")
        break
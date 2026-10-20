def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def modulo(a, b):
    if b == 0:
        return "Cannot calculate modulo by zero"
    return a % b


while True:
    print("\n=== CLI Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulo")
    print("Q. Quit")

    choice = input("Choose an operation: ").strip().lower()

    if choice == "q":
        print("Goodbye!")
        break

    if choice not in ("1", "2", "3", "4", "5"):
        print("Invalid choice. Please select 1, 2, 3, 4, 5, or Q.")
        continue

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        continue

    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", subtract(num1, num2))
    elif choice == "3":
        print("Result:", multiply(num1, num2))
    elif choice == "4":
        print("Result:", divide(num1, num2))
    elif choice == "5":
        print("Result:", modulo(num1, num2))

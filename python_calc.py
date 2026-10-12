def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b


def check_even_odd(n):
    if n != int(n):
        return "Please enter a whole number for even/odd check."
    if int(n) % 2 == 0:
        return f"{int(n)} is Even"
    return f"{int(n)} is Odd"


def percentage(a, b):
    if b == 0:
        return "Error: Cannot calculate percentage of zero!"
    return f"{a} is {(a / b) * 100:.2f}% of {b}"


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a number.")


def show_menu():
    print("\n===== CALCULATOR MENU =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Check Even/Odd")
    print("6. Calculate Percentage")
    print("7. Exit")


def main():
    print("Welcome to the Python Calculator!")

    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break

        if choice in ("1", "2", "3", "4"):
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            if choice == "1":
                print("Result:", add(a, b))
            elif choice == "2":
                print("Result:", subtract(a, b))
            elif choice == "3":
                print("Result:", multiply(a, b))
            else:
                print("Result:", divide(a, b))

        elif choice == "5":
            n = get_number("Enter a number: ")
            print("Result:", check_even_odd(n))

        elif choice == "6":
            a = get_number("Enter the number: ")
            b = get_number("Enter the total/base number: ")
            print("Result:", percentage(a, b))

        else:
            print("Invalid choice. Please pick a number from 1 to 7.")


if __name__ == "__main__":
    main()
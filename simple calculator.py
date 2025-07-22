# Simple Calculator using Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

print("--- Simple Calculator ---")

while True:
    print("\nChoose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
         print("Exiting calculator. Thankyou!")
         break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        print("Result =", add(num1, num2))

    elif choice == '2':
        print("Result =", subtract(num1, num2))

    elif choice == '3':
        print("Result =", multiply(num1, num2))

    elif choice == '4':
        print("Result =", divide(num1,num2))

    else:
        print("Invalid input. Try again.")
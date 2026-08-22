# CODSOFT Task 2 - Calculator

print("================================")
print("        SIMPLE CALCULATOR")
print("================================")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    result = num1 + num2
    print("\nResult:", result)

elif choice == "2":
    result = num1 - num2
    print("\nResult:", result)

elif choice == "3":
    result = num1 * num2
    print("\nResult:", result)

elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        print("\nResult:", result)
    else:
        print("\nError: Cannot divide by zero.")

else:
    print("\nInvalid choice.")

print("\nThank you for using the calculator!")

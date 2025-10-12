#Nested_try_except
try:
    # Outer try block
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Outer exception: Cannot divide by zero!")
    try:
        # Nested try block inside except
        print("Trying to divide by 0 again...")
        print(10 / 0)
    except ZeroDivisionError:
        print("Inner exception: Still cannot divide by zero!")
except ValueError:
    print("Please enter a valid integer.")

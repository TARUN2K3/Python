#Raising_Exception_using_raise_keyword
def check_age(age):
    if age < 18:
        # Manually raise a ValueError
        raise ValueError("Age must be at least 18 to register.")
    else:
        print("Age is valid. Registration successful.")

# Main program
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except ValueError as ve:
    print("Caught an exception:", ve)

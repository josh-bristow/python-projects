# The Complete Python 3 Course: Beginner to Advanced Project #1

def addition(x, y):
    """This function adds two numbers together"""
    return x + y


def subtraction(x, y):
    """This function subtracts y from x"""
    return x - y


def multiply(x, y):
    """This function multiplies two numbers together"""
    return x * y


def division(x, y):
    """This function divides x by y"""
    return x / y


print("*The Basic Bristow Calculator*")
print("Select an operation:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

selection = int(input("Choose 1, 2, 3 or 4: "))

num1 = int(input("Choose your first value: "))
num2 = int(input("Choose your second value: "))

if selection == 1:
    print(num1, "+", num2, "=", addition(num1, num2))
elif selection == 2:
    print(num1, "-", num2, "=", subtraction(num1, num2))
elif selection == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))
elif selection == 4:
    print(num1, "/", num2, "=", division(num1, num2))
else:
    print("You did not select a correct operation, you bring shame to your forefathers! :(")


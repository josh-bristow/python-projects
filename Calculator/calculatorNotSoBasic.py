# The Complete Python 3 Course: Beginner to Advanced Project #1 (Advanced)

import re

print("Magic Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True


def perform_math():
    global run
    global previous
    equation =""
    if previous == 0:
        equation = input("Enter Equation: ")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print("Goodbye, human!")
        run = False
    else:
        equation = re.sub('[a-zA-Z,:.()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    perform_math()

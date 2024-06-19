import art

print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    """Does operations on numbers"""
    keepGoing = True
    n1 = float(input("Enter first number: "))

    while keepGoing:
        operation = input("Pick an operation (+, -, /, *): ")
        n2 = float(input("Enter second number: "))

        calculation_function = operations[operation]
        result = calculation_function(n1, n2)
        print(f"{n1} {operation} {n2} = {result}")

        next_step = input(f"Type 'y' to keep calculating with {result}, type 'n' to start a new calculation, type 'quit' to terminate the program: ")

        if next_step == 'y':
            n1 = result
        elif next_step == 'n':
            keepGoing = False
            calculator()
        else:
            keepGoing = False

calculator()
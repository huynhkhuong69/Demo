import error

def calculator(number1, number2, operator):
 """This function operations will compute addition (+), 
    subtraction(-), multiplication(*), division(/), integer division (//) and power(**) operation.
    Function should take three parameters in this order: number1, number2, operator
    Calculator function should return the result of the operation but if the operation was invalid return False
    The function called parse_input(), which will take input from the user and call the calculator function
    The parse_input() function job should take input from user, parse input from user,
    and pass user inpt to calculator() function
 """

    try:
        if operator == "+":
            return number1 + number2
        elif operator == "-":
            return number1 - number2
        elif operator == "*":
            return number1 * number2
        elif operator == "/":
            return number1 / number2
        elif operator == "//":
            return number1 // number2
        elif operator == "**":
            return number1 ** number2
        else:
            return False
    except error:
        return False

def parse_input():
    expr = input("Enter equation: ")
    first_number, operator, second_number = expr.split()
    first_number = float(first_number)
    second_number = float(second_number)
    print(calculator(first_number, second_number, operatori))

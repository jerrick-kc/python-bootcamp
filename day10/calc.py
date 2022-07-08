from art import logo

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
    print(logo)
    num1 = float(input("What is the first number? "))
    continue_program = True
    while continue_program:
        for operation in operations:
            print(operation)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number? "))

        function_call = operations[operation_symbol]
        answer = function_call(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        run_again = input(f"Would you like to keep working with {answer}? Enter 'y' or 'n': ")

        if run_again == 'y':
            num1 = answer
        else:
            continue_program = False
            calculator()


calculator()

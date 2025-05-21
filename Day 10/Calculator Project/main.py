def add(n1, n2):
    return n1 + n2

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x/y

calculations = {
    "*": multiply,
    "/": divide,
    "-": subtract,
    "+": add
}

def calculator():
    calculate = False
    output = float(input("Input Number"))
    while not calculate:
        operation = input("Input Operation ['+', '-', '*' or '/']").strip()
        sec_number = float(input("Input Number"))
        output = calculations[operation](output, sec_number)
        if input("Calculate? (Y/N)").lower() == "y":
            print(output)
            calculate = True
        else:
            continue



calculator()


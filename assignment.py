

user_input = "Which operation do you want to carry out today??"
def calculator(a, b):
    global user_input
    if user_input == '+':
        return f"The result of the operation is {a + b}"
    elif user_input == '-':
        return f"The result of the operation is {a - b}"
    if user_input == '*':
        return f"The result of the operation is {a * b}"
    if user_input == '/':
        return f"The result of the operation is {a / b}"
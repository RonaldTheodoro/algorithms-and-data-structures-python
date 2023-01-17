from algorithms.stacks.stack import Stack


def base_converter(decimal_number, base):
    stack = Stack()
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = int(decimal_number)
    base_string = ""

    if not (base >= 2 and base <= 36):
        return ""

    while number > 0:
        stack.push(number % base)
        number = number // base

    while not stack.is_empty():
        base_string += digits[stack.pop()]

    return base_string

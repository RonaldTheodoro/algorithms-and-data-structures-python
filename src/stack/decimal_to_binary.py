from algorithms.stacks.stack import Stack


def decimal_to_binary(decimal_number):
    stack = Stack()
    number = int(decimal_number)
    binary_string = ""

    while number > 0:
        stack.push(number % 2)
        number = number // 2

    while not stack.is_empty():
        binary_string += str(stack.pop())

    return binary_string

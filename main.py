from operator import index

def operation(arr, index):
    global new_number
    left = float(arr[index - 1])
    op = arr[index]
    right = float(arr[index + 1])

    if op == "*":
        new_number = left * right
    elif op == "/":
        new_number = left / right
    elif op == "%":
        new_number = left % right
    elif op == "+":
        new_number = left + right
    elif op == "-":
        new_number = left - right

    arr[index] = new_number
    arr.pop(index - 1)
    arr.pop(index)
    return calculate(arr)

def calculate(expression):
    chars = None
    if isinstance(expression, str):
        chars = parse_the_expression(expression.replace(" ", ""))
    else: chars = expression

    if len(chars) == 1:
        return chars[0]

    if "(" in chars:
        start = chars.index("(")
        end = start

        while chars[end] != ")":
            end += 1

        inside = chars[start + 1:end]
        result = calculate(inside)

        chars[start] = result
        for i in range(end, start, -1):
            del chars[i]

        return calculate(chars)

    if "*" in chars or "/" in chars or "%" in chars:
        index = next(i for i, ch in enumerate(chars) if ch in ["*", "/", "%"])
        return operation(chars, index)
    else:
        index = next(i for i, ch in enumerate(chars) if ch in ["-", "+"])
        return operation(chars, index)

def parse_the_expression(expression):
    chars = []
    number = ""

    for i, ch in enumerate(expression):
        if ch.isnumeric() or ch == ".":
            number += ch
        elif ch == "-" and (
                i == 0 or expression[i - 1] in "+-*/%("
        ):
            number += ch
        else:
            if number:
                chars.append(number)
                number = ""
            chars.append(ch)

    if number:
        chars.append(number)

    return chars

print("result is: " + str(calculate("2 * 5 + ( 15 / 5 ) - (12 - 2 + 4) * (-3 / 1 * -2+1000 / 3445)")))
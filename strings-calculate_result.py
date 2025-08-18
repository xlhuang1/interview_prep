# Given a string of an arithmetic expression, composed of numbers, '+' and '*', calculate the result.

def calculate_result(s):
    parts = []
    current = ""

    # go through string and get delimiters and numbers
    for c in s:
        if c in {"+", "*"}:
            parts.append(current)
            parts.append(c)
            current = ""
        else:
            current += c
    parts.append(current)

    total = 0
    term = int(parts[0])

    i = 1
    while i < len(parts):
        op = parts[i]
        num = int(parts[i+1])

        if op == "*":
            term *= num
        else: # +
            total += term
            term = num
        i += 2
    return total + term

print(calculate_result("2*4+5+8*7"))
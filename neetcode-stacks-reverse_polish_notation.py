# You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation

# Return the integer that represents the evaluation of the expression.
#
# The operands may be integers or the results of other operations.
# The operators include '+', '-', '*', and '/'.
# Assume that division between integers always truncates toward zero.

# Input: tokens = ["1","2","+","3","*","4","-"]
# Output: 5
# Explanation: ((1 + 2) * 3) - 4 = 5

def eval_RPN(tokens):
    stack = []
    for x in tokens:
        if x not in "+-*/":
            stack.append(int(x))
        elif x == '+':
            term = stack.pop()
            term += stack.pop()
            stack.append(term)
        elif x == '-':
            neg = stack.pop()
            term = stack.pop()
            stack.append(term-neg)
        elif x == '*':
            term = stack.pop()
            term *= stack.pop()
            stack.append(term)
        elif x == '/':
            denom = stack.pop()
            numerator = stack.pop()
            stack.append(int(numerator/denom))
    return stack[-1]


print(eval_RPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
# A bracket is any of the following characters: (, ), {, }, [, or ].
# We consider two brackets to be matching if the first bracket is an open-bracket, e.g., (, {, or [, and the second bracket is a close-bracket of the same type. That means ( and ), [ and ], and { and } are the only pairs of matching brackets.

def isBalanced(s):
    # Write your code here
    char_stack = []

    lefts = {'(' : ')', '[' : ']', '{' : '}'}
    for x in s:
        if x in lefts.keys():
            char_stack.append(lefts[x])
        else: # a closing bracket - check if r_stack has match and then remove from both stacks
            if not char_stack:
                return False
            if x != char_stack.pop():
                return False
    return not char_stack

print(isBalanced('{[(])}'))
print(isBalanced('{{[[(())]]}}'))
print(isBalanced('][]'))
print(isBalanced('[][[['))
print(isBalanced('(([]){)'))

print("Expected: FTFFF")
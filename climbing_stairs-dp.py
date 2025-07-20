# dynamic programming - count the number of ways to climb a staircase n steps high.
# you can only climb one or two steps at a time

# try one
# def ways(n, memo=None):
#     if memo == None:
#         memo = []
#
#     if n in memo:
#         return memo[n]
#
#     if n == 1:
#         # base case n = 1 -> one way to climb [1]
#         memo[n] = 1
#         return 1
#     elif n == 2:
#         # base case n = 2 -> [1, 1] or [2]
#         memo[n] = 2
#         return 2
#     else:
#         memo[n] = ways(n-1, memo) + ways(n-2, memo)
#         return ways(n-1, memo) + ways(n-2, memo)

# try two
def ways(n, memo=None):
    if memo == None:
        memo = {}

    if n in memo:
        return memo[n]

    if n == 1:
        # base case n = 1 -> one way to climb [1]
        memo[n] = 1
    elif n == 2:
        # base case n = 2 -> [1, 1] or [2]
        memo[n] = 2
    else:
        memo[n] = ways(n-1, memo) + ways(n-2, memo)

    return memo[n]

# bottom up iterative approach - uses O(1) space because it does not use recursion for the calls
def ways(n, memo=None):
    if memo == None:
        memo = {}

    if n == 1:
        # base case n = 1 -> one way to climb [1]
        memo[n] = 1
        return 1
    elif n == 2:
        # base case n = 2 -> [1, 1] or [2]
        memo[n] = 2
        return 2
    else:
        for x in range(3,n):
            memo[x] = memo[x-1] + memo[x-2]
        return memo[n]

# try 3 bottom up iterative
def ways(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    memo = {1: 1, 2: 2}
    for x in range(3, n+1):
        memo[x] = memo[x - 1] + memo[x - 2]
    return memo[n]
# this is still O(n) space

# try 4 O(1) space
def ways(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    first = 1
    second = 2
    for x in range(3, n+1):
        third = first + second
        first = second
        second = third
    return second

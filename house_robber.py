# house robber - max amount of money made from robbing houses, given cannot rob adjacent houses
# dynamic programming approach - break problem down into smaller problem
# brute force O(2^n)

# try one
# def rob_helper(i, houses):
#     if i == len(houses):
#         return 0
#     elif i == len(houses) - 1:
#         return houses[i]
#
#     return max(rob_helper(i+1, houses), houses[i] + rob_helper(i+2, houses))
#
#
# def rob(houses):
#     i = 0
#     x = 0
#
#     while i < len(houses) + 1:
#         x = rob_helper(i, houses)
#         i += 1
#     return x


# try 2
def rob_helper(i, houses):
    if i >= len(houses):
        return 0

    return max(rob_helper(i+1, houses), houses[i] + rob_helper(i+2, houses))


def rob(houses):
    return rob_helper(0, houses)


# try 3 with memoization
def rob_helper(i, houses, loot=None):
    if i >= len(houses):
        return 0
    if loot == None:
        loot = {}

    if i in loot:
        return loot[i]

    loot[i] = max(rob_helper(i+1, houses, loot), houses[i] + rob_helper(i+2, houses, loot))
    return loot[i]


def rob(houses):
    return rob_helper(0, houses)


# try 4 bottom up with O(1) space
def rob(houses):
    if not houses:
        return 0
    if len(houses) == 1:
        return houses[0]
    if len(houses) == 2:
        return max(houses[0], houses[1])

    prev2 = houses[0]
    prev1 = max(houses[0], houses[1])

    for i in range(2, len(houses)):
        current = max(prev1, prev2 + houses[i])
        prev2 = prev1
        prev1 = current

    return prev1
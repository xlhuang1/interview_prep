# Suppose we have a list of N numbers, and repeat the following operation until we're left with only a single number:
# Choose any two numbers and replace them with their sum. Moreover, we associate a penalty with each operation equal to the value of the new number,
# and call the penalty for the entire list as the sum of the penalties of each operation.
#
# For example, given the list [1, 2, 3, 4, 5],
# we could choose 2 and 3 for the first operation,
# which would transform the list into [1, 5, 4, 5] and incur a penalty of 5.
#
# The goal in this problem is to find the highest possible penalty for a given input.

import heapq

def getTotalTime(arr):
    if len(arr) == 0:
        return 0

    max_heap = [-x for x in arr]
    heapq.heapify(max_heap)

    penalty = 0

    while len(max_heap) > 1:
        x1 = -heapq.heappop(max_heap)
        x2 = -heapq.heappop(max_heap)

        penalty += x1 + x2
        heapq.heappush(max_heap, -(x1 + x2))
    return penalty

print(getTotalTime([1, 2, 3, 4, 5]))
print(getTotalTime([4, 2, 1, 3]))
print(getTotalTime([1, 1, 1, 3, 1]))
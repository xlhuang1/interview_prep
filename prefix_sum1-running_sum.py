# Running Sum of 1D Array
# Leetcode 1480
# Input: [1,2,3,4] → Output: [1,3,6,10]
# 👉 Straightforward running sum. Your warm-up drill.

def running_sum(array):
    result = []
    prefix_sum = 0
    for x in array:
        prefix_sum += x
        result.append(prefix_sum)
    return result
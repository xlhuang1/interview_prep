# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals k
# array is integers positive, negative, or zero.
# array is unordered
# subarrays must be contiguous

def subarrays_sum(k, nums):
    prefix_sum = {0 : 1}
    current_sum = 0
    counts = 0

    for x in nums:
        current_sum += x
        counts += prefix_sum.get(current_sum-k, 0)
        prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

    return counts
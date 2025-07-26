# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
# Example -
# Input: nums = [0,1,0,1,1,1,0]
# Output: 6
# Explanation: The subarray [0,1,0,1,1,1] has three 0s and three 1s.

# The core idea for solving this in O(n) time is to:
#
# Treat 0s as -1 and 1s as +1.
#
# Maintain a running prefix sum while scanning the array.
#
# Use a hash map to store the first index where each prefix sum value was seen.
#
# If the same prefix sum is seen again, the subarray between those indices has an equal number of 0s and 1s (because the deltas cancel out).

def count_largest_contiguous_subarray(array):
    prefix_sum = 0
    # prefix_sum_hash = {0 : 0} <- incorrect - should be -1 to account for balanced array that starts with 0
    prefix_sum_hash = {0 : -1}
    max_len = 0

    for i, n in enumerate(array):
        inc = 1 if n == 1 else -1
        prefix_sum += inc
        if prefix_sum in prefix_sum_hash:
            max_len = max(max_len, i - prefix_sum_hash[prefix_sum])
        else:
            prefix_sum_hash[prefix_sum] = i
    return max_len

print(count_largest_contiguous_subarray([0, 1]))
print(count_largest_contiguous_subarray([1, 0]))
print(count_largest_contiguous_subarray([1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1]))

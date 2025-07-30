# Binary Subarrays with Sum
# Leetcode 930
# Count subarrays of 0/1 array with exact sum S.
# 👉 Prefix sum with hashmap.

def binary_subarray_sum(bin_array, S):
    prefix_sum = 0
    seen = {0 : 1}
    count = 0

    for x in bin_array:
        prefix_sum += x
        if prefix_sum - S in seen:
            count += seen[prefix_sum - S]
        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
    return count
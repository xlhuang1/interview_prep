# Contiguous Array
# Leetcode 525
# Longest subarray with equal 0s and 1s.
# 👉 Convert 0 → -1 and use prefix sum map.

def longest_equal_subarray(bin_array):
    prefix_sum = 0
    seen_sums = {0 : -1}
    max_len = 0

    for i, x in enumerate(bin_array):
        # seen sums is hash of prefix sum and index seen. we want to get the longest subarray with equal 1s and 0s
        prefix_sum = prefix_sum + 1 if x == 1 else -1
        if prefix_sum in seen_sums:
            max_len = max(max_len, i - seen_sums[prefix_sum])
        else:
            # this needs to be in else statement because we only want to store the first occurrence of each prefix sum
            # we want the LONGEST distance between indices
            seen_sums[prefix_sum] = i
    return max_len
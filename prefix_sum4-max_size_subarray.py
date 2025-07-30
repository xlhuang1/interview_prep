# Maximum Size Subarray Sum Equals K
# Leetcode 325
# length of longest subarray sum to k.
# Like above, but return the length of the longest subarray.
# 👉 Subtle prefix map + first-seen index logic.

def max_size_subarray(nums, k):
    max_seen = 0
    prefix_sum = 0
    seen = {0 : -1} # array index where prefix sum is seen

    for i, x in enumerate(nums):
        prefix_sum += x
        if prefix_sum - k in seen:
            max_seen = max(i - seen[prefix_sum -k], max_seen)
        seen[prefix_sum] = i
    return max_seen
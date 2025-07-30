# Number of Subarrays with Bounded Maximum
# Leetcode 795
# Tricky edge case with constraints L ≤ max ≤ R.
# 👉 Sliding window + prefix sum strategy.

# You are given an integer array nums and two integers left and right.
# You need to count the number of contiguous subarrays such that the maximum element in that subarray is between left and right (inclusive).

#  We want to count how many subarrays end at each index i where the max element in the subarray is within [left, right].

# If nums[i] > right, then we cannot include i or any subarray ending at i. So, the window is broken — we reset.
# If nums[i] < left, the value is too small to start a valid subarray by itself, but it can extend a previously valid subarray.
# If left <= nums[i] <= right, then it’s a valid high value and we can form new valid subarrays ending at i.

def subarrays_with_max(nums, left, right):
    start = 0
    prev_valid_count = 0
    total = 0

    for i, x in enumerate(nums):
        if x > right:
            start = i + 1
            prev_valid_count = 0
        elif x < left:
            total += prev_valid_count
        else:  # x in [left, right]
            prev_valid_count = i - start + 1
            total += prev_valid_count
    return total

# Range Sum Query – Immutable
# Leetcode 303
# design a class with a method sumRange(i, j) that returns the sum of elements from index i to j, inclusive.
# The array itself doesn't change after initialization.

class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.prefix_sums = {}
        self.current_sum = 0
        for i, x in enumerate(nums):
            self.current_sum += x
            self.prefix_sums[i] = self.current_sum


    def sumRange(self, i, j):
        # returns sum of elements from index i to j
        if 0 <= i <= j < len(self.nums):
            sum_j = self.prefix_sums[j]
            sum_i = self.prefix_sums[i]
            return sum_j - sum_i + self.nums[i]
        else:
            raise ValueError("invalid values for i or j")

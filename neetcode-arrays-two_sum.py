# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
#
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
#
# Return the answer with the smaller index first.


# brute force - O(n^2) time and O(1) space
def two_sum_brute(nums, target):
    for i, x in enumerate(nums):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

def two_sum(nums, target):
    prevMap = {}  # val -> index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i


print(two_sum([3, 4, 5, 6], 7))
print(two_sum([4, 5, 6], 10))
print(two_sum([5, 5], 10))
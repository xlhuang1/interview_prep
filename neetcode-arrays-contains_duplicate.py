# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

def has_duplicate(nums):
    if len(nums) > len(set(nums)):
        return True
    return False

print(has_duplicate([1, 1, 2, 3]))
print(has_duplicate([1, 4, 2, 3]))

# You are given an integer array nums and an integer target.
# Return the number of unique pairs (i, j) where i < j such that nums[i] + nums[j] == target.
#
# You may assume nums can contain duplicates and negative values.
#
# Your solution should be efficient for large arrays (e.g., up to 10⁵ elements).

def sum_of_pairs(target, nums):
    sorted_list = []
    for i, x in enumerate(nums):
        sorted_list.append((x, i))
    # sort the list of val, index pairs
    sorted_list.sort()

    # indices for left and right
    left = 0
    right = 1
    sum_pair = 0
    result = []

    while left < len(nums) - 1:
        if right >= len(nums):
            left += 1
            right = left + 1
            continue
        sum_pair = sorted_list[left][0] + sorted_list[right][0]
        if sum_pair == target:
            result.append((min(sorted_list[left][1], sorted_list[right][1]), max(sorted_list[left][1], sorted_list[right][1])))
            right += 1
        elif sum_pair < target:
            right += 1
        else: # sum_pair > target
            left += 1
            right = left + 1
    return result


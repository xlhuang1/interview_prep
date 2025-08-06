# given a 0-indexed integer array nums of length n and an integer target,
# return the number of pairs (i, j) where 0<=i < j < n and nums[i] + nums[j] < target

# brute force O(n^2) - outer loop i, inner loop j, increment sum

# optimized solution O(n log n) - sort nums,
# then O(n) pass using two pointers left and right

def two_sums(nums, target):
    nums.sort()
    left = 0
    right = len(nums) - 1

    count = 0

    while left < right:
        if nums[left] + nums[right] < target:
            count += right - left
            left += 1
        else:
            right -= 1
    return count


# Given:
# nums: a list of integers (may contain duplicates)
# target: an integer
#
# Return:
# A list of all pairs of values (nums[i], nums[j]) where:
# 0 ≤ i < j < len(nums)
# nums[i] + nums[j] < target
#
# Constraints:
# Each (i, j) is unique due to i < j
# If nums has duplicates, multiple (i, j) pairs may still map to the same values, but those are treated as distinct unless deduplication is explicitly required (not here)
# Output can include repeated values, as long as i < j

def two_sums_pairs(nums, target):
    i = 0
    pairs = []

    for i in range(len(nums)-1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] < target:
                pairs.append((nums[i], nums[j]))
    return pairs

def two_sums_pairs_optimized(nums, target):
    # put nums into a list with original index
    nums_indexed = []
    results = []
    for i, x in enumerate(nums):
        nums_indexed.append((x, i))
    nums_indexed.sort()

    left = 0
    right = len(nums_indexed)-1

    while left < right:
        if nums_indexed[left][0] + nums_indexed[right][0] < target:
            for j in range(left+1, right+1):
                if nums_indexed[left][1] < nums_indexed[j][1]:
                    results.append((nums_indexed[left][0], nums_indexed[j][0]))
                else:
                    results.append((nums_indexed[j][0], nums_indexed[left][0]))
            left += 1
        else:
            right -= 1
    return results

print(two_sums_pairs_optimized([1, 2, 5, 3, 3, 2], 7))


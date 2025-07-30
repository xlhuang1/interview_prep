# You're given an integer array nums and an integer k. A subarray of nums is a contiguous segment — possibly the whole array or as small as a single element.
# We define a "nice" subarray as one that contains exactly k odd numbers.
# Your task is to write a function that returns the number of nice subarrays in nums.

def find_k_odds(nums, k, right):
    num_odds = 0
    while num_odds < k:
        right += 1
        if right > len(nums)-1:
            return 0 # edge case - less than k odd numbers in nums
        if nums[right] % 2 == 1:
            if first_odd == 0:
                first_odd = right
            num_odds += 1
    return right

def find_next_odd(nums, starting_right):
    right = starting_right+1
    while nums[right] % 2 == 0 and right < len(nums) - 1:
        right += 1
    return right

def find_nice_subarrays(nums, k):
    results = 0
    left = 0
    right = -1 #initialize -1 because I want to add index at start of while loop
    first_odd = 0

    while left < len(nums)-1:
        right_at_kth = find_k_odds(nums, k, right)

        # find next odd starting at index of kth odd
        next_odd = find_next_odd(nums, right_at_kth)

        nice_lefts = range(left, first_odd)
        nice_rights = range(right_at_kth, next_odd)
        results = results + len(nice_lefts) * len(nice_rights)
        # first pass

        while left < len(nums)-1:
            left = find_next_odd(nums, first_odd)
            nice_lefts = range(first_odd, left)
            right_at_kth = next_odd
            next_odd = find_next_odd(nums, next_odd)
            nice_rights = range(right_at_kth, next_odd)
            results = results + len(nice_lefts) * len(nice_rights)
            first_odd = left
    return results


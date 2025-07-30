# Given an integer array nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

def subarray_sum_k(nums, k):
    prefix_sum = 0
    seen = {0 : 1}
    count = 0

    for i, x in enumerate(nums):
        prefix_sum += x
        if prefix_sum - k in seen:
            count += seen[prefix_sum - k]
        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
    return count



# tests
test_cases = [
    # (nums, k, expected_output)
    ([1, 3, 1, 3, 5, 7], 4, 3),
    ([1, 1, 1], 2, 2),
    ([1, 2, 3], 3, 2),
    ([1, -1, 1], 1, 3),
    ([3, 4, 7, 2, -3, 1, 4, 2], 7, 4),
    ([1], 1, 1),
    ([1], 0, 0),
    ([0, 0, 0], 0, 6),  # multiple overlapping subarrays
    ([], 0, 0),
    ([-1, -1, 1], 0, 1),
]

for i, (nums, k, expected) in enumerate(test_cases):
    result = subarray_sum_k(nums, k)
    assert result == expected, f"Test case {i + 1} failed: expected {expected}, got {result}"
print("All test cases passed.")
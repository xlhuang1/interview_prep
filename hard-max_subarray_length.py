# You are given a list of integers nums and an integer k. Return the length of the longest subarray whose sum is less than or equal to k.

from bisect import bisect_left, insort

def max_subarray_length(nums, k: int) -> int:
    prefix_sum = 0
    max_len = 0

    # Running list of (prefix_sum, index), kept sorted by prefix_sum
    running = [(0, -1)]  # initial prefix 0 at index -1

    for i, num in enumerate(nums):
        prefix_sum += num
        target = prefix_sum - k

        # Binary search for smallest prefix_sum ≥ target
        idx = bisect_left(running, (target, float('-inf')))

        if idx < len(running):
            _, j = running[idx]
            max_len = max(max_len, i - j)

        # Insert current (prefix_sum, index) into the running list
        # Only insert if this is the first time we've seen this prefix_sum
        # or it occurs earlier than any previously recorded index
        if not running or prefix_sum < running[-1][0]:
            insort(running, (prefix_sum, i))

    return max_len
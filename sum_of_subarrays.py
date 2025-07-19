def subarray_sums(nums, k):
    current_sum = 0
    prefix_counts = {0: 1}
    count = 0

    for x in nums:
        current_sum += x

        count += prefix_counts.get(current_sum-k, 0)

        prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1

    return count
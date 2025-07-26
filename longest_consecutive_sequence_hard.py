# Given an unsorted array of integers nums, return the length of the longest sequence of consecutive elements.
# You must solve the algorithm in O(n) time

# Input: nums = [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].

def longest_consecutive_sequence(array):
    num_set = set(array)
    result = 0

    for n in array:
        if n-1 not in num_set:
            current_num = n
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            result = max(result, current_streak)
    return result


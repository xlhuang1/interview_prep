# initial try:

# def longest_num_sequence(nums):
#     num_set = set(nums)
#     longest = 0
#
#     for num in num_set:
#         if num-1 not in num_set:
#             curr_num = num
#             curr_seq_len = 1
#             consecutive = True
#             while consecutive is True:
#                 curr_num += 1
#                 if curr_num in num_set:
#                     curr_seq_len += 1
#                     if curr_seq_len > longest:
#                         longest = curr_seq_len
#                 else:
#                     consecutive = False
#     return longest

# corrected code:
def longest_num_sequence(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num-1 not in num_set:
            curr_num = num
            curr_seq_len = 1

            while curr_num + 1 in num_set:
                curr_seq_len += 1
                curr_num += 1

            longest = max(longest, curr_seq_len)

    return longest



print(longest_num_sequence([100, 4, 200, 1, 3, 2]))  # Output: 4 (1-2-3-4)
print(longest_num_sequence([1, 2, 0, 1]))            # Output: 3 (0-1-2)
print(longest_num_sequence([]))
print(longest_num_sequence([1]))



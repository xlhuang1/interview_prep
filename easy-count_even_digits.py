# Given an array nums of integers, return how many of them contain an even number of digits.

def count_even_digits(nums):
    count = 0
    for x in nums:
        char_array = str(x)
        if len(char_array) % 2 == 0:
            count += 1
    return count

# Given a list of integers, return how many of them contain an even number of even digits.
def count_even_digit_evens(nums):
    count = 0
    for x in nums:
        inner_count = 0
        char_array = str(x)
        if any(int(c) % 2 != 0 for c in char_array):
            continue
        if len(char_array) % 2 == 0:
            count += 1
    return count
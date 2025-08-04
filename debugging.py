str = "anna"

def is_palindrome(s):
    return s == s[::-1]


def remove_duplicates(nums):
    if not nums:
        return 0

    write_index = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[write_index] = nums[i]
            write_index += 1
    return nums[:write_index]

print(remove_duplicates([1, 1, 3, 4, 5, 6, 6, 7, 7]))
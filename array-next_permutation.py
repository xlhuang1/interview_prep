# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
#
# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
# More formally, if all the permutations of the array are sorted in one container according to their lexicographical order,
# then the next permutation of that array is the permutation that follows it in the sorted container.
#
# If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).
#
# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.
#
# The replacement must be in place and use only constant extra memory.

def reverse_in_place(arr, i):
    # reverse array in place from i+1 to end
    l = i + 1
    r = len(arr) - 1

    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    return arr

def next_permutation(arr):
    if len(arr) < 2:
        return arr

    pivot = None
    for i in range(len(arr)-2, -1, -1):
        if arr[i] < arr[i+1]:
            pivot = i
            break

    if pivot == None:
        return reverse_in_place(arr, -1)

    j = len(arr) - 1
    while arr[j] <= arr[pivot]:
        j -= 1

    arr[pivot], arr[j] = arr[j], arr[pivot]
    return reverse_in_place(arr, pivot)


print(next_permutation([1, 4, 3, 2]))
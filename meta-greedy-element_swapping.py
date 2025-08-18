# Given a sequence of n integers arr, determine the lexicographically smallest sequence which may be obtained from it after performing at most k element swaps,
# each involving a pair of consecutive elements in the sequence.
# Note: A list x is lexicographically smaller than a different equal-length list y if and only if,
# for the earliest index at which the two lists differ, x's element at that index is smaller than y's element at that index.
#
# Example 1
# n = 3
# k = 2
# arr = [5, 3, 1]
# output = [1, 5, 3]
# We can swap the 2nd and 3rd elements, followed by the 1st and 2nd elements, to end up with the sequence [1, 5, 3].
# This is the lexicographically smallest sequence achievable after at most 2 swaps.
#
# Example 2
# n = 5
# k = 3
# arr = [8, 9, 11, 2, 1]
# output = [2, 8, 9, 11, 1]
# We can swap [11, 2], followed by [9, 2], then [8, 2].

def findMinArray(arr, k):

    def scan_for_smallest(array, start, cost):
        #
        # constraint of the problem is that elements of arr is in range [1, 1000000]
        smallest_seen = 1000001
        idx_of_smallest = len(array) + 1
        for i, x in enumerate(array):
            if i < cost + 1:
                if x < smallest_seen:
                    idx_of_smallest = i
                    smallest_seen = x
        return idx_of_smallest + start

    def slide_m_to_j(array, j, m):
        replace = array.pop(m)
        array.insert(j, replace)
        return array

    j = 0
    result = arr[:]
    while k > 0 and j < len(arr):
        m = scan_for_smallest(result[j:], j, k)
        if m == j:
            j += 1
            continue
        k = k - (m-j)  # recompute remaining cost
        result = slide_m_to_j(result, j, m)
        j += 1
    return result

print(findMinArray([5, 6, 1, 3], 3))

# You're given a list of n integers arr[0..(n-1)]. You must compute a list output[0..(n-1)] such that,
# for each index i (between 0 and n-1, inclusive), output[i] is equal to the median of the elements arr[0..i] (rounded down to the nearest integer).
#
# The median of a list of integers is defined as follows. If the integers were to be sorted, then:
#
# If there are an odd number of integers, then the median is equal to the middle integer in the sorted order.
# Otherwise, if there are an even number of integers, then the median is equal to the average of the two middle-most integers in the sorted order.
# round down for averages

import heapq

def findMedian(arr):
    output = [0] * len(arr)

    left = [] # max heap on left
    right = [] # min heap on right

    for i, x in enumerate(arr):
        heapq.heappush(left, -x)

        if len(right) > 0 and (-left[0] > right[0]):
            heapq.heappush(right, -heapq.heappop(left))
        if len(left) - len(right) > 1:
            # rebalance to right
            heapq.heappush(right, -heapq.heappop(left))
        if len(right) > len(left):
            heapq.heappush(left, -heapq.heappop(right))

        if len(left) > len(right):
            # odd number of items
            output[i] = -left[0]
        else:
            # even number of items
            output[i] = (-left[0] + right[0])//2
    return output

print(findMedian([5, 15, 1, 3]))
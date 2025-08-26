# Largest Triple Products
# You're given a list of n integers arr[0..(n-1)]. You must compute a list output[0..(n-1)] such that, for each index i (between 0 and n-1, inclusive),
# output[i] is equal to the product of the three largest elements out of arr[0..i] (or equal to -1 if i < 2, as arr[0..i] then includes fewer than three elements).
# Note that the three largest elements used to form any product may have the same values as one another, but they must be at different indices in arr.
# Signature
# int[] findMaxProduct(int[] arr)
# Input
# n is in the range [1, 100,000].
# Each value arr[i] is in the range [1, 1,000].
# Output
# Return a list of n integers output[0..(n-1)], as described above.
# Example 1
# n = 5
# arr = [1, 2, 3, 4, 5]
# output = [-1, -1, 6, 24, 60]
# The 3rd element of output is 3*2*1 = 6, the 4th is 4*3*2 = 24, and the 5th is 5*4*3 = 60.
# Example 2
# n = 5
# arr = [2, 1, 2, 1, 2]
# output = [-1, -1, 4, 4, 8]
# The 3rd element of output is 2*2*1 = 4, the 4th is 2*2*1 = 4, and the 5th is 2*2*2 = 8.


import heapq

# this is O(n log n) - can improve
def findMaxProduct(arr):
    output = []
    max_heap = []

    for x in arr:
        heapq.heappush(max_heap, -x) # simulate max heap by adding neg values
        if len(max_heap) < 3:
            output.append(-1)
        else:
            # take the largest 3 items out of max_heap, multiply, then append to output
            # then push back onto max_heap
            x1 = -heapq.heappop(max_heap)
            x2 = -heapq.heappop(max_heap)
            x3 = -heapq.heappop(max_heap)

            output.append(x1 * x2 * x3)
            heapq.heappush(max_heap, -x1)
            heapq.heappush(max_heap, -x2)
            heapq.heappush(max_heap, -x3)
    return output

def findMaxProduct_improved(arr):
    output = []
    min_heap = [] # min heap of three largest values

    for x in arr:
        heapq.heappush(min_heap, x)

        if len(min_heap) < 3:
            output.append(-1) # expected behavior for arrays of len < 3
        elif len(min_heap) > 3:
            heapq.heappop(min_heap) # maintain min_heap at size 3

        if len(min_heap) == 3:
            output.append(min_heap[0] * min_heap[1] * min_heap[2])
    return output



# tests
print(findMaxProduct_improved([1, 2, 3, 4, 5]))
print(findMaxProduct_improved([1, 2]))
print(findMaxProduct_improved([1, 2, 5, 3, 5]))
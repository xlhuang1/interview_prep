# Given an integer array nums and an integer k, return the k most frequent elements.
# You must solve it in O(n log k) time complexity or better.

# You may assume the array is non-empty.
# You must return exactly k elements.
# The order of output does not matter.

import heapq

def top_k_frequent(k, nums):
    frequency_map = {}
    k_most_frequent = []

    for x in nums:
        frequency_map[x] = frequency_map.get(x, 0) + 1
    for x, freq in frequency_map.items():
        if len(k_most_frequent) < k:
            heapq.heappush(k_most_frequent, (freq, x))
        elif freq >= k_most_frequent[0][0]:
            heapq.heappop(k_most_frequent)
            heapq.heappush(k_most_frequent, (freq, x))

    response = []
    while k_most_frequent:
        item = heapq.heappop(k_most_frequent)
        response.append(item[1]) # append the element to the answer
    return response
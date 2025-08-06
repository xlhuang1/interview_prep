# Given a string s, rearrange the characters of s so that no two adjacent characters are the same.
# return any valid rearrangement
# if no such arrangement is possible, return an empty string ""

import heapq

def reorganize_string(input_string):
    frequency_count = {}
    for c in input_string:
        frequency_count[c] = frequency_count.get(c, 0) + 1

    max_freq_heap = []
    for item in frequency_count.items():
        heapq.heappush(max_freq_heap, (-item[1], item[0]))

    result_str = []
    while len(max_freq_heap) >= 2:
        item_a = heapq.heappop(max_freq_heap)
        item_b = heapq.heappop(max_freq_heap)

        result_str.append(item_a[1])
        result_str.append(item_b[1])

        if -item_a[0] - 1 > 0:
            heapq.heappush(max_freq_heap, (-(-item_a[0]-1), item_a[1]))
        if -item_b[0] - 1 > 0:
            heapq.heappush(max_freq_heap, (-(-item_b[0]-1), item_b[1]))
    if len(max_freq_heap) == 1:
        if result_str[-1] == max_freq_heap[0][1] or -max_freq_heap[0][0] > 1:
            return ""
        else:
            result_str.append(max_freq_heap[0][1])
    return ''.join(result_str)

print(reorganize_string("asdfaaa"))
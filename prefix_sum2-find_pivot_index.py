# Find Pivot Index
# Leetcode 724
# Return the index where left sum = right sum.
# 👉 Think carefully about full sum – current prefix sum.

def find_pivot_index(array):
    full_sum = sum(array)
    prefix_sum = 0
    for i, x in enumerate(array):
        if full_sum - prefix_sum - x == prefix_sum:
            return i
        prefix_sum += x
    return None
# You’re given an array sticks where each value represents the length of a stick.
# You can connect any two sticks:
# The cost is equal to the sum of their lengths
# The resulting stick has that new length
# You can repeat this until there is only one stick
# 👉 Return the minimum total cost to connect all sticks.

# optimal solution - use a min heap and always connect the two smallest sticks O(n log n) time

import heapq

def connect_sticks(sticks):
    sticks_min_heap = []

    for stick in sticks:
        heapq.heappush(sticks_min_heap, stick)

    cost = 0
    while len(sticks_min_heap) >= 2:
        stick1 = heapq.heappop(sticks_min_heap)
        stick2 = heapq.heappop(sticks_min_heap)

        new_stick = stick1 + stick2
        cost += new_stick
        heapq.heappush(sticks_min_heap, new_stick)

    return cost

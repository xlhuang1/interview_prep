# You’re given a list of stones, each with a positive integer weight.
# Each turn:
# Pick the two heaviest stones.
# Smash them:
# If equal: both are destroyed.
#
# If not: the heavier one becomes heavier - lighter, and is added back.
#
# Repeat until one or zero stones remain.

import heapq

def last_stone_weight(stones):
    stone_max_heap = []
    for stone in stones:
        heapq.heappush(stone_max_heap, -stone)

    while len(stone_max_heap) >= 2:
        stone1 = -heapq.heappop(stone_max_heap)
        stone2 = -heapq.heappop(stone_max_heap)

        if stone1 - stone2 > 0:
            heapq.heappush(stone_max_heap, -(stone1-stone2))
    if len(stone_max_heap) == 1:
        return -stone_max_heap[0]
    else:
        return 0
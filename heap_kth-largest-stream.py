# Design a class called KthLargest that finds the k-th largest element in a stream of integers.
# Implement the class with the following methods:
#
# class KthLargest:
#     def __init__(self, k: int, nums: List[int]):
#         ...
#
#     def add(self, val: int) -> int:
#         ...

import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums
        self.k_largest_seen = []

        for x in nums:
            if not self.k_largest_seen or len(self.k_largest_seen) < k:
                heapq.heappush(self.k_largest_seen, x)
            else:
                if x > self.k_largest_seen[0]:
                    # need to add x to heap
                    heapq.heappop(self.k_largest_seen)
                    heapq.heappush(self.k_largest_seen, x)

    def add(self, val: int) -> int:
        # check if heap is full - if not insert to heap
        if len(self.k_largest_seen) < self.k:
            heapq.heappush(self.k_largest_seen, val)
        elif val >= self.k_largest_seen[0]:
            heapq.heappop(self.k_largest_seen)
            heapq.heappush(self.k_largest_seen, val)

        return self.k_largest_seen[0]
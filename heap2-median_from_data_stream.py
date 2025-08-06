# Design a class that supports:
# addNum(num): adds a number to the stream
# findMedian(): returns the median of all elements so far
#
# You must optimize for real-time performance—logarithmic time per insertion.

# keep track of 2 heaps - max heap on left, min heap on right
# median if left == right size will be avg of both heads
# median if left > right will be head of left

import heapq

class MedianFinder:
    def __init__(self):
        self.left = []  # max heap of left side of data stream
        self.right = []  # min heap of right side of data stream

    def addNum(self, num):
        heapq.heappush(self.left, -num)

        if self.right and -self.left[0] > self.right[0]:
            # move to the right
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)

        if len(self.left) > len(self.right) + 1:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        elif len(self.right) > len(self.left):
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)

    def findMedian(self):
        if len(self.left) == len(self.right):
            return (self.right[0]-self.left[0])/2  # using minus because self.left is max heap
        else:
            return (-self.left[0])

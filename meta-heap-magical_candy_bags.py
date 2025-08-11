# You have N bags of candy. The ith bag contains arr[i] pieces of candy, and each of the bags is magical!
# It takes you 1 minute to eat all of the pieces of candy in a bag (irrespective of how many pieces of candy are inside), and as soon as you finish, the bag mysteriously refills.
# If there were x pieces of candy in the bag at the beginning of the minute, then after you've finished you'll find that floor(x/2) pieces are now inside.
#
# You have k minutes to eat as much candy as possible. How many pieces of candy can you eat?

import heapq

def maxCandies(arr, k):
    if k == 0 or len(arr) == 0:
        return 0

    candy_heap = [-x for x in arr] # max heap implemented using push of negative values
    heapq.heapify(candy_heap)

    eaten = 0
    for i in range(k):
        x = -heapq.heappop(candy_heap)
        if x == 0:
            # largest bag contains 0 candy but k large
            break

        eaten += x
        heapq.heappush(candy_heap, -(x//2))

    return eaten

# Given a permutation arr of 1..N (1 ≤ N ≤ 8), return the minimum number of operations to sort it ascending, where one operation is: choose indices i ≤ j and reverse arr[i..j].

# Example
# arr = [3, 1, 2] → 2
#
# Reverse [1,2] → [3,2,1]
#
# Reverse [3,2,1] → [1,2,3]

# It looks like a sorting problem on the surface, but the state space is what makes it a graph problem.
#
# Each permutation of 1..N is a node in the graph.
# There’s an edge between two permutations if you can get from one to the other by doing a single reversal of a subarray.
#
# The goal is to find the shortest path from the starting permutation to the sorted permutation [1, 2, …, N].
# Because N ≤ 8, there are at most 8! = 40,320 nodes — small enough to BFS over.
#
# BFS on this graph guarantees the minimum number of operations because it explores all permutations at distance k before moving to k+1.
# So: sorting rules define valid edges, BFS finds the minimum number of edges from start to goal.

from collections import deque

def minOperations(arr):
    start = tuple(arr)
    goal = tuple(sorted(arr))
    if start == goal:
        return 0

    # Standard BFS over permutation states
    q = deque([(start, 0)])
    seen = {start}

    while q:
        state, dist = q.popleft()

        # Generate all neighbors by reversing any subarray [i..j], i < j
        n = len(state)
        for i in range(n):
            for j in range(i + 1, n):
                # reverse slice i..j
                nxt = state[:i] + tuple(reversed(state[i:j+1])) + state[j+1:]
                print("state: "+str(state))
                print("nxt: "+str(nxt))
                if nxt in seen:
                    continue
                if nxt == goal:
                    return dist + 1
                seen.add(nxt)
                q.append((nxt, dist + 1))

    # Should never happen for a permutation space reachable by reversals
    return -1


print(minOperations([1, 4, 2, 3, 5]))
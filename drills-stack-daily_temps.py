# Given an array temps where temps[i] is the daily temperature,
# return an array wait where wait[i] is the number of days after day i you must wait until a warmer temperature.
# If there’s no future day for which this is possible, set wait[i] = 0.

from typing import List

def daily_temperatures(temps: List[int]) -> List[int]:
    """
    Monotonic decreasing stack of indices.
    For each day i, pop all previous days j with temps[i] > temps[j],
    and set wait[j] = i - j. Equal temps do not pop (not warmer).
    Time: O(n), Space: O(n).
    """
    n = len(temps)
    wait = [0] * n
    stack = []  # indices with strictly decreasing temps

    for i, t in enumerate(temps):
        # Resolve any earlier cooler days
        while stack and t > temps[stack[-1]]:
            j = stack.pop()
            wait[j] = i - j
        stack.append(i)

    return wait

# Quick checks:
print(daily_temperatures([73,74,75,71,69,72,76,73]))  # [1,1,4,2,1,1,0,0]
print(daily_temperatures([30,40,50,60]))              # [1,1,1,0]
# print(daily_temperatures([30,60,90]))                 # [1,1,0]
# print(daily_temperatures([90,80,70]))                 # [0,0,0]
# print(daily_temperatures([70]))                       # [0]
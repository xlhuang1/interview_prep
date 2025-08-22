# You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.
#
# Return the number of distinct ways to climb to the top of the staircase.

def climb_stairs(n):
    cache = [-1] * n

    def climb_stairs_helper(i):
        if i >= n:
            return 1 if i == n else 0
        if cache[i] != -1:
            return cache[i]
        cache[i] = climb_stairs_helper(i+1) + climb_stairs_helper(i+2)
        return cache[i]

    return climb_stairs_helper(0)

print(climb_stairs(8))
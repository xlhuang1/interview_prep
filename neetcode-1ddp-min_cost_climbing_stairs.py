# You are given an array of integers cost where cost[i] is the cost of taking a step from the ith floor of a staircase. After paying the cost, you can step to either the (i + 1)th floor or the (i + 2)th floor.
# You may choose to start at the index 0 or the index 1 floor.
# Return the minimum cost to reach the top of the staircase, i.e. just past the last index in cost.

def min_cost_climbing_stairs(cost):
    memo = [-1] * len(cost)

    def climb_stairs_helper(i):
        if i >= len(cost):
            return 0
        if memo[i] != -1:
            return memo[i]
        memo[i] = cost[i] + min(climb_stairs_helper(i+1), climb_stairs_helper(i+2))
        return memo[i]

    return min(climb_stairs_helper(0), climb_stairs_helper(1))

print(min_cost_climbing_stairs([1, 2, 3, 4]))
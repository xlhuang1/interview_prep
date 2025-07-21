# rob houses recap / retry

# def rob_helper(i, nums):
#     if i == 0:
#         return nums[i]
#     if i == 1:
#         return max(nums[0], nums[i])
#
#     current_loot = 0
#     for i in range(2, len(nums)):
#         current_loot += max(rob_helper(i-2) + nums[i], rob_helper(i-1))
#     return current_loot
#
# def rob(nums):
#     rob_helper(0, nums)


# fixed
def rob_helper(i, nums, memo):
    if memo is None:
        memo = {}

    if i >= len(nums):
        return 0
    if i in memo:
        return memo[i]

    loot = max(nums[i] + rob_helper(i+2, nums, memo), rob_helper(i+1, nums, memo))
    memo[i] = loot
    return loot

def rob(nums):
    return rob_helper(0, nums, None)

def test_rob():
    # Case 1: Standard case
    assert rob([1, 2, 3, 1]) == 4  # Rob house 1 and 3 (1 + 3)

    # Case 2: Larger numbers
    assert rob([2, 7, 9, 3, 1]) == 12  # Rob house 1 and 3 (7 + 3) or 2 and 4 (2 + 9 + 1)

    # Case 3: Only one house
    assert rob([5]) == 5

    # Case 4: Two houses
    assert rob([2, 1]) == 2  # Rob house 0

    # Case 5: All equal
    assert rob([10, 10, 10, 10]) == 20  # Rob house 0 and 2 (or 1 and 3)

test_rob()
# Given an integer array nums of unique elements, return all possible subsets (the power set).
#
# The solution set must not contain duplicates.

def subsets(nums):
    result = []
    path = []

    def dfs(idx):
        if idx == len(nums):
            result.append(path[:])
            return
        path.append(nums[idx])
        dfs(idx + 1)
        path.pop()
        dfs(idx + 1)

    dfs(0)
    return result
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        helper(nums, 0, [], ans)  # Call the helper function with initial values
        return ans

def helper(nums, start_index, res, ans):
    # Base case: When we have processed all elements
    if start_index == len(nums):
        ans.append(list(res))  # Add the current subset
        return

    # Choice 1: Take the current element
    res.append(nums[start_index])
    helper(nums, start_index + 1, res, ans)

    # Backtrack: Undo the choice of taking the current element
    res.pop()

    # Choice 2: Do not take the current element
    helper(nums, start_index + 1, res, ans)

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # Initialize memoization dictionary
        memo = {}
        
        # Call the helper function with the last index
        return helper(nums, len(nums) - 1, memo)

def helper(nums, idx, memo):
    # Base case: When index is out of bounds
    if idx < 0:
        return 0
    
    # Check if the result for this index is already computed
    if idx in memo:
        return memo[idx]
    
    # Base case: When there's only one house to rob
    if idx == 0:
        return nums[0]
    
    # Recursive cases with memoization
    pick = nums[idx] + helper(nums, idx - 2, memo)
    not_pick = helper(nums, idx - 1, memo)
    
    # Compute and store the result in the memoization dictionary
    memo[idx] = max(pick, not_pick)
    
    return memo[idx]

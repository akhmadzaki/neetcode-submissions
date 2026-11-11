class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        def helper(sub):
            n = len(sub)
            if n == 1:
                return sub[0]
            
            dp = [0] * n
            dp[0] = sub[0]
            dp[1] = max(sub[0], sub[1])
            
            for i in range(2, n):
                dp[i] = max(dp[i-1], sub[i] + dp[i-2])
            
            return dp[-1]
        


        return max(helper(nums[:-1]), helper(nums[1:]))
        
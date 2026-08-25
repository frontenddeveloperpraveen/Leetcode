class Solution:
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if(n == 0):
            return 0
        if(n==1):
            return nums[0]
        if(n==2):
            return max(nums[0],nums[1])
        def normal(nums):
            n = len(nums)
            if(n==0):return 0
            if(n==1): return nums[0]
            if(n==2): return max(nums[0],nums[1])
            dp=[0]*(n)
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])
            for house in range(2,n):
                dp[house] = max(dp[house-1],(dp[house-2]+nums[house]))
            print(dp)
            return max(dp[n-1],dp[n-2])    

        one = normal(nums[1:n])    
        two = normal(nums[0:n-1])    
        return max(one,two)
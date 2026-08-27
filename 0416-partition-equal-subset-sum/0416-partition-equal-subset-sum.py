class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        Sum = sum(nums)
        if Sum % 2 != 0:
            return False
        target = Sum // 2
        # memo = {}        
        # def Check(idx, cur_sum):
        #     if((idx,cur_sum) in memo):
        #         return memo[(idx,cur_sum)]
        #     if(cur_sum == Target):
        #         memo[(idx,cur_sum)] = True
        #         return True
            
        #     if(idx<0):
        #         memo[(idx,cur_sum)] = False
        #         return False
        #     # Take
        #     if(Check(idx-1,cur_sum+nums[idx])):
        #         memo[(idx,cur_sum)] = True
        #         return True
        #     #No Take
        #     if(Check(idx-1,cur_sum)):
        #         memo[(idx,cur_sum)] = True
        #         return True

        #     memo[(idx,cur_sum)] = False
        #     return False
        # return Check(len(nums)-1,0)
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n)]
        for idx in range(n):
            dp[idx][0] = True
        if nums[0] <= target:
            dp[0][nums[0]] = True
        for idx in range(1, n):
            for cur_sum in range(1, target + 1):

                # Don't take nums[idx]
                not_take = dp[idx - 1][cur_sum]

                # Take nums[idx]
                take = False
                if nums[idx] <= cur_sum:
                    take = dp[idx - 1][cur_sum - nums[idx]]

                # Either choice should work
                dp[idx][cur_sum] = take or not_take

        return dp[n - 1][target]
 


            
        
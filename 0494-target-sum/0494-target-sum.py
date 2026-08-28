class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Two stattes -> + or - 
        memo = {}
        def TargetSum(n,count):
            if(n < 0):
                if(count == target):
                    return 1
                return 0
            if((n,count) in memo):
                return memo[(n,count)]
            # Try Plus
            plus = TargetSum(n-1,count+nums[n])

            #Try Minus

            neg = TargetSum(n-1,count-nums[n])

            memo[(n,count)] = plus+neg
            
            return plus+neg
        return TargetSum(len(nums)-1,0)
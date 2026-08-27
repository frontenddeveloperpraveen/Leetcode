class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        Sum = sum(nums)
        if Sum % 2 != 0:
            return False
        Target = Sum // 2
        memo = {}        
        def Check(idx, cur_sum):
            if((idx,cur_sum) in memo):
                return memo[(idx,cur_sum)]
            if(cur_sum == Target):
                memo[(idx,cur_sum)] = True
                return True
            
            if(idx<0):
                memo[(idx,cur_sum)] = False
                return False
            # Take
            if(Check(idx-1,cur_sum+nums[idx])):
                memo[(idx,cur_sum)] = True
                return True
            #No Take
            if(Check(idx-1,cur_sum)):
                memo[(idx,cur_sum)] = True
                return True

            memo[(idx,cur_sum)] = False
            return False
        return Check(len(nums)-1,0)
            

            
        
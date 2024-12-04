class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i,n in enumerate(nums):
            balance = target - n
            if(balance in prev):
                return([prev[balance],i])
            else:
                prev[n] = i
        else:
            return
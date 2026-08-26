class Solution:
    def canCross(self, stones: List[int]) -> bool:
        laststone = stones[-1]
        stones = set(stones)
        memo = {}
        def dfs(stone,jump):
            if(stone == laststone):
                return True
            
            if(stone not in stones):
                return False

            if((stone,jump) in memo):
                return memo[(stone,jump)]

            # 3 Ways 
            for nextjump in (jump-1,jump,jump+1):
                if(nextjump <=0):
                    continue
                
                nextstone = nextjump + stone

                if(dfs(nextstone,nextjump)):
                    memo[(nextstone,nextjump)] = True
                    return True
            memo[(stone,jump)] = False
            return False
        return dfs(0,0)
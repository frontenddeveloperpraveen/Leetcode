class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def dfs(idx,pos):
            if(idx >= len(triangle)  or pos >= len(triangle[idx])):
                return 0
            if((idx,pos) in memo):
                return memo[(idx,pos)]
            val = triangle[idx][pos]
            nidx = dfs(idx+1,pos)
            n1idx = dfs(idx+1,pos+1)
            memo[(idx,pos)] = min(nidx,n1idx) + val
            return memo[(idx,pos)]
        return dfs(0,0)
            
        
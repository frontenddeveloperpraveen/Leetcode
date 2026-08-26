class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # memo = {}
        # def dfs(idx,pos):
        #     if(idx >= len(triangle)  or pos >= len(triangle[idx])):
        #         return 0
        #     if((idx,pos) in memo):
        #         return memo[(idx,pos)]
        #     val = triangle[idx][pos]
        #     nidx = dfs(idx+1,pos)
        #     n1idx = dfs(idx+1,pos+1)
        #     memo[(idx,pos)] = min(nidx,n1idx) + val
        #     return memo[(idx,pos)]
        # return dfs(0,0)

        # Tabulation

        n = len(triangle)

        dp = [[0]*n for _ in range(n)]

        dp[0][0] = triangle[0][0]

        for col in range(1,n):
            dp[0][col] = float("inf")
        for row in range(1,n):
            dp[row][0] = dp[row-1][0] + triangle[row][0]
        for row in range(1,n):
            for col in range(1,n):
                if(col >= len(triangle[row])):
                    dp[row][col] = float('inf')
                else:
                    dp[row][col] = min(dp[row-1][col], dp[row-1][col-1]) + (triangle[row][col])
            
        return min(dp[-1])
            
        
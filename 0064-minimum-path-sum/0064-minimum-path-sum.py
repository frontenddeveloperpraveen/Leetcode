class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Possible action right and down
        memo = {}
        def dfs(m,n):
            if(m < 0 or n <0):
                memo[(m,n)] = float('inf')
                return float('inf')
                
            if((m,n) in memo):
                return memo[(m,n)]
            if(m==0 and n==0):
                memo[(m,n)] = grid[m][n]
                return memo[(m,n)]
            
            

            # left movie 
            left = dfs(m,n-1)

            #Down
            up = dfs(m-1,n)

            memo[(m,n)] = min(left,up) + grid[m][n]
            return memo[(m,n)]

        return dfs(len(grid)-1,len(grid[0])-1)


        
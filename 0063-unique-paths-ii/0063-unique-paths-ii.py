class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        def dfs(a,b):
            if((a,b) in memo):
                return memo[(a,b)]
            if(a==0 and b==0 and obstacleGrid[a][b] != 1):
                memo[(a,b)] = 1
                return 1
            if(a<0 or b<0):
                memo[(a,b)] = 0
                return 0
            if(obstacleGrid[a][b] == 1):
                memo[(a,b)] = 0
                return 0
            memo[(a,b)] = dfs(a-1,b) + dfs(a,b-1)
            return memo[(a,b)]
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        return dfs(m-1,n-1)
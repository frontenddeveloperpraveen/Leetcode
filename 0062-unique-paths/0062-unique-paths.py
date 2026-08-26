class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def bfs(a,b):
            if(a==0 and b==0):
                memo[(a,b)] = 1
                return 1
            if(a < 0 or b<0):
                memo[(a,b)] = 0
                return 0
            if((a,b) in memo):
                return memo[(a,b)]
            memo[(a,b)] = bfs(a-1,b) + bfs(a,b-1)
            return memo[(a,b)]
        return bfs(m-1,n-1)
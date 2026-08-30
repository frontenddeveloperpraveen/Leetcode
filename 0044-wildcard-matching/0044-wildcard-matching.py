class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # memo = {}
        # def Find(i,j):
        #     # Base cases skip
        #     if i == len(s) and j == len(p):
        #         return True
        #     if i == len(s):
        #         return all(x == '*' for x in p[j:])

            
        #     if(j >= len(p)):
        #         return False
            
        #     if((i,j) in memo):
        #         return memo[(i,j)]

        #     if(p[j] == "*"):
        #         way1 = Find(i,j+1)
        #         way2 = Find(i+1,j)
        #         memo[(i,j)] =  way1 or way2
        #         return way1 or way2

        #     if(s[i] == p[j] or p[j] == "?"):
        #         memo[(i,j)] = Find(i+1,j+1) 
        #         return  memo[(i,j)]
            
        #     memo[(i,j)] = False
        #     return False

        # return Find(0,0)

        dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
        dp[0][0] = True
        for j in range(1, len(p) + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1]

        for i in range(0,len(s)):
            for j in range(0,len(p)):
                if(s[i] == p[j] or p[j] == "?"):
                    dp[i+1][j+1] = dp[i][j]
                if(p[j] == "*"):
                    dp[i+1][j+1] = dp[i+1][j] or dp[i][j+1]
            
        return dp[-1][-1]
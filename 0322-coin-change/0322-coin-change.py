class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        n = len(coins)
        # def check(n, total):
        #     if total == amount:
        #         return 0

        #     if total > amount or n < 0:
        #         return float("inf")
            
        #     if((n,total) in memo):
        #         return memo[(n,total)]

        #     take = 1 + check(n, total + coins[n])
        #     not_take = check(n - 1, total)

        #     memo[(n,total)] = min(take, not_take)
        #     return memo[(n,total)]
        # ans = check(len(coins)-1,0)
        # return -1 if ans  == float("inf") else ans 

    # Tabulation
        dp = [[0]*(amount+1) for _ in range(n)]
        
        # Column
        e = coins[0]
        
        for i in range(1,amount+1):
            if(i%e == 0):
                dp[0][i] = i//e
            else:
                dp[0][i] = float('inf')
        
        for j in range(1,n):
            for total in range(1,amount+1):
                if coins[j] <= total:
                    take = 1 + dp[j][total - coins[j]]
                else:
                    take = float("inf")
                not_take = dp[j - 1][total]
                dp[j][total] = min(take, not_take)
                
        ans = dp[n-1][-1]
        return -1 if ans == float("inf") else ans
        
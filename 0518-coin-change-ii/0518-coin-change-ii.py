class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # memo = {}
        # def Check(idx,count):
        #     if(count == amount):
        #         return 1

        #     if(count > amount):
        #         return 0
            
        #     if(idx < 0):
        #         return 0

        #     if((idx,count) in memo):
        #         return memo[(idx,count)]
        #     # Take and stay or No Take and go

        #     take = Check(idx,count+coins[idx])
            
        #     notake = Check(idx-1,count)

        #     memo[(idx,count)] = take+notake

        #     return take+notake

        # return Check(len(coins)-1,0)
        
        # Tabulation
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n)]
        e = coins[0]
        for idx in range(n):
            dp[idx][0] = 1
        for i in range(1,amount+1):
            if(i%e == 0):
                dp[0][i] = 1

        for idx in range(1,n):
            for count in range(1,amount+1):
                take = 0
                if(coins[idx] <= count):
                    take = dp[idx][count-coins[idx]] 
                notake = dp[idx-1][count]
                dp[idx][count] = take+notake

        return dp[-1][-1]


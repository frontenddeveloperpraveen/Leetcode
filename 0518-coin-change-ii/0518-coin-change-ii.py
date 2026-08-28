class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def Check(idx,count):
            if(count == amount):
                return 1

            if(count > amount):
                return 0
            
            if(idx < 0):
                return 0

            if((idx,count) in memo):
                return memo[(idx,count)]
            # Take and stay or No Take and go

            take = Check(idx,count+coins[idx])
            
            notake = Check(idx-1,count)

            memo[(idx,count)] = take+notake

            return take+notake

        return Check(len(coins)-1,0)
        
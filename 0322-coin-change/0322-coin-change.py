from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def check(n, total):
            if total == amount:
                return 0

            if total > amount or n < 0:
                return float("inf")

            take = 1 + check(n, total + coins[n])
            not_take = check(n - 1, total)

            return min(take, not_take)
        ans = check(len(coins)-1,0)
        return -1 if ans  == float("inf") else ans 
class Solution:
    def climbStairs(self, n: int) -> int:
        #Tablulation
        if(n <= 2): return n #Base
        table = [0]*(n+1)
        table[1] = 1
        table[2] = 2

        for step in range(3,n+1):
            table[step] = table[step-1]+table[step-2]
        
        return table[n]

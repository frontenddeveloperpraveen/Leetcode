from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def Find(i,j):
            if(j == len(t)):
                return 1
            if(i == len(s)):
                return 0
            
            # No Take
            a = Find(i+1,j)

            b = 0

            if(s[i] == t[j]):

                b = Find(i+1,j+1)
            
            return a+b
        return Find(0,0)
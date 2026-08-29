from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def Find(i,j):
            if i >= len(word1):
                return len(word2) - j

            if j >= len(word2):
                return len(word1) - i
            
            if(word1[i] == word2[j]):
                return Find(i+1,j+1)
            
            s1 = Find(i+1,j)
            s2 = Find(i,j+1)

            return min(s1,s2) + 1
        
        return Find(0,0)
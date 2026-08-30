from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def Find(i,j):
            if(i >= len(word1)):
                return len(word2[j:])
            
            if(j >= len(word2)):
                return len(word1[i:])


            if(word1[i] == word2[j]):
                return 0 + Find(i+1,j+1)
            
            insert = Find(i,j+1)
            delete = Find(i+1,j)
            replace = Find(i+1,j+1)

            return min(insert,delete,replace) + 1
        return Find(0,0)
class Solution:
    def minInsertions(self, s: str) -> int:
        memo = {}
        def Find(i,j):
            if(i>j):
                return 0
            if(i == j):
                return 0
            if((i,j) in memo):
                return memo[(i,j)]
            if(s[i] == s[j]):
                return Find(i+1,j-1)

            left = Find(i+1,j)        
            right = Find(i,j-1)

            memo[(i,j)] = 1+ min(left,right)
            return 1+ min(left,right)
        return Find(0,len(s)-1)
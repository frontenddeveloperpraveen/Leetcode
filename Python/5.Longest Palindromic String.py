class Solution:
    def palindrome(self, s):
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        Max = 0
        final = ""
        
        for i in range(len(s)):
            pointer1, pointer2 = i, i
            while pointer1 >= 0 and pointer2 < len(s) and s[pointer1] == s[pointer2]:
                temp = s[pointer1:pointer2+1]
                if len(temp) > Max:
                    Max = len(temp)
                    final = temp
                pointer1 -= 1
                pointer2 += 1
            pointer1, pointer2 = i, i + 1
            while pointer1 >= 0 and pointer2 < len(s) and s[pointer1] == s[pointer2]:
                temp = s[pointer1:pointer2+1]
                if len(temp) > Max:
                    Max = len(temp)
                    final = temp
                pointer1 -= 1
                pointer2 += 1

        return final

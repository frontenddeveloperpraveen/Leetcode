class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if(x < 0):
            negative = True
            x = abs(x)
        temp = x
        final=0
        while(temp):
            last = temp % 10 
            final = (final * 10) + last
            temp = temp // 10
        if(negative):
            final = 0 - final
        if(not (final >= (-2**31) and final <= (2**31 - 1))):
            return 0
        return final


        
        
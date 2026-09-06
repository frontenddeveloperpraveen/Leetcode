class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        def Triangle(Rows):
            if(Rows == 1):
                result.append([1])
                return [1]
            if(Rows == 2):
                Triangle(Rows-1)
                result.append([1,1])
                return [1,1]
            
            prev = Triangle(Rows-1)
            
            temp = [1]*Rows

            for i in range(1,len(prev)):
                temp[i] = prev[i-1]+prev[i]
            
            result.append(temp[:])
            return temp
        Triangle(numRows)
        return result
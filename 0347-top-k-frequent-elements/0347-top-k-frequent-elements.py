class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for element in nums:
            if(element in hashmap):
                hashmap[element]+=1
            else:
                hashmap[element] = 1

        dict_elements = list(hashmap.items())
        dict_elements.sort(key=lambda x:x[1],reverse=True)
        result = []
        for keys in dict_elements:
            if k == 0:
                break
            result.append(keys[0])
            k-=1
        
        return result
        
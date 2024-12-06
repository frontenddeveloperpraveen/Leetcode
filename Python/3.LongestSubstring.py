class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tracker = set()
        max_element = 0
        pointer = 0

        for i in range(len(s)):
            while s[i] in tracker:
                tracker.remove(s[pointer])
                pointer +=1
            tracker.add(s[i])
            max_element = max(max_element, i - pointer+1)

        return max_element
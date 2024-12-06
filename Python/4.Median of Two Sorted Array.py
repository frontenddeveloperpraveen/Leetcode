class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        total_length = len(nums1) + len(nums2)
        if total_length % 2 == 1:
            return self.findNthValue(nums1, nums2, total_length // 2 + 1)
        else:
            mid1 = self.findNthValue(nums1, nums2, total_length // 2)
            mid2 = self.findNthValue(nums1, nums2, total_length // 2 + 1)
            return (mid1 + mid2) / 2

    def findNthValue(self, nums1, nums2, n):
        if len(nums1) > len(nums2):
            return self.findNthValue(nums2, nums1, n)
        
        if not nums1:
            return nums2[n - 1] 
        if n == 1:
            return min(nums1[0], nums2[0])  
        idx1 = min(n // 2, len(nums1))  
        idx2 = n - idx1  
        val1 = nums1[idx1 - 1]  
        val2 = nums2[idx2 - 1]  
        if val1 <= val2:
            return self.findNthValue(nums1[idx1:], nums2, n - idx1)
        else:
            return self.findNthValue(nums1, nums2[idx2:], n - idx2)

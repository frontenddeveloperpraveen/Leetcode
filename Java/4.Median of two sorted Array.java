class Solution {
    int findNindex(int[] nums1, int[] nums2, int n){
        // Find the Index of Element N
        if(nums1.length > nums2.length){
            return findNindex(nums2,nums1,n);
        }
        if(nums1.length == 0){
            return nums2[n-1];
        }
        if(n == 1){
            return Math.min(nums1[0],nums2[0]);
        }

        int half1 = Math.min(n/2,nums1.length);

        int half2 = n - half1;

        int nums1val = nums1[half1 -1];

        int nums2val = nums2[half2 -1];

        if(nums1val < nums2val){
            return findNindex(Arrays.copyOfRange(nums1, half1, nums1.length),nums2,n-half1);
        }else{
            return findNindex(nums1,Arrays.copyOfRange(nums2, half2, nums2.length),n-half2);
        }
    
        


    }
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int length = nums1.length + nums2.length;
        int val = length / 2;
        if(length % 2 == 0){
            //Even Length
            
            return (findNindex(nums1,nums2,val) + findNindex(nums1,nums2,val+1)) / 2.0;


        }else{
            //Odd Length
            return findNindex(nums1,nums2,val+1)/1.0;

        }    
    }
}
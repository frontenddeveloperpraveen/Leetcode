import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> prev = new HashMap<>();

        for(int i = 0; i<nums.length;i++){
            
            int balance = target - nums[i];

            if(prev.containsKey(balance))
                return new int[] {prev.get(balance),i};
            else
                prev.put(nums[i],i);   
        }
        return new int[] {};
    
    }
    
    }

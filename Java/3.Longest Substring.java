class Solution {
    public int lengthOfLongestSubstring(String s) {
     Map <Character,Integer> Tracker = new HashMap<>();
     int max = 0;
     int pointer = 0;


     for(int i=0; i<s.length();i++){

        while(Tracker.containsKey(s.charAt(i))){

            Tracker.remove(s.charAt(pointer));

            pointer++;
        }
        Tracker.put(s.charAt(i), i);
        max = Math.max(max, i - pointer + 1);

     }

     return max;


    }
}
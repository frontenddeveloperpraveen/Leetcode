class Solution {
    public int reverse(int x) {
        int temp = x;
        long final_num = 0;
        int last = 0;
        while(temp != 0){
            last = temp % 10;
            final_num = final_num * 10 + last;
            temp = temp / 10; 
        }
        if(final_num > Integer.MAX_VALUE || final_num < Integer.MIN_VALUE){
            return 0 ;
        }
        return (int) final_num;

    }
}
class Solution {
    public String longestPalindrome(String s) {
        int pointer1 = 0;
        int pointer2 = 0;
        String temp = "";
        String finals = "";
        int max = 0;

        for (int i = 0; i < s.length(); i++) {
            // Odd-length palindrome
            pointer1 = pointer2 = i;

            while (pointer1 >= 0 && pointer2 < s.length() && s.charAt(pointer1) == s.charAt(pointer2)) {
                temp = s.substring(pointer1, pointer2 + 1);
                if (max < temp.length()) {
                    max = temp.length();
                    finals = temp;
                }
                pointer1--;
                pointer2++;
            }

            // Even-length palindrome
            pointer1 = i;
            pointer2 = i + 1;

            while (pointer1 >= 0 && pointer2 < s.length() && s.charAt(pointer1) == s.charAt(pointer2)) {
                temp = s.substring(pointer1, pointer2 + 1);
                if (max < temp.length()) {
                    max = temp.length();
                    finals = temp;
                }
                pointer1--;
                pointer2++;
            }
        }

        return finals;
    }
}

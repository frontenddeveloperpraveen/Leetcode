class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode Final = new ListNode();
        ListNode Temp = Final;
        int Carry = 0;

        while(l1 != null || l2 != null || Carry != 0){
        
        int a = l1!=null ? l1.val : 0;
        int b = l2!=null ? l2.val : 0;

        int sum = a + b + Carry;

        Carry = sum / 10;

        int ans = sum % 10;

        ListNode newnode = new ListNode(ans);

        Temp.next = newnode;

        Temp = Temp.next;

        if (l1 != null) l1 = l1.next;
        if (l2 != null) l2 = l2.next;

        }
        return Final.next;
        
    }
}
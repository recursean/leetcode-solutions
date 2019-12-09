class Pr19 {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode idx = null;
        ListNode ptr = head;
        ListNode ret = head;
        int ctr = 0;

        while(ptr.next != null) {
            ptr = ptr.next;

            if(ctr++ >= n - 1) {
                if(idx == null) {
                    idx = head;
                }
                else {
                    idx = idx.next;  
                }
            }
        }

        if(idx == null || ctr == n - 1) {
            ret = head.next;
            head = null;
        }

        else {
            try {
                idx.next = idx.next.next;
            }
    
            catch(NullPointerException e) {
                idx.next = null;
            }
        }

        return ret;
    }
}
class Pr21 {
    class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }

    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode t1 = l1;
        ListNode t2 = l2;
        ListNode head;
        ListNode curr;

        if(t1 != null) {
            if(t2 == null || t1.val <= t2.val) {
                head = t1;
                curr = t1;
                t1 = t1.next;
            }
            else {
                head = t2;
                curr = t2;
                t2 = t2.next;
            }
        }
        else if(t2 != null) {
            head = t2;
            curr = t2;
            t2 = t2.next;
        }

        while(t1 != null && t2 != null) {
            if(t1 == null || (t2 != null && t1.val >= t2.val)) {
                curr.next = t2;
                curr = curr.next;

                if(t2.next == null) {
                    t2 = null;
                }
                else {
                    t2 = t2.next;
                }
            }
            else {
                curr.next = t1;
                curr = curr.next;

                if(t1.next == null) {
                    t1 = null;
                }
                else {
                    t1 = t1.next;
                }
            }
        }

        return head;
    }

    public static void main(String[] args) {
       
    }
}



import java.util.ArrayList;

// Given a singly linked list L: L0→L1→…→Ln-1→Ln,
// reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

// You may not modify the values in the list's nodes, only nodes itself may be changed.

public class DailyChallenge082020 {

    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public void reorderList(ListNode head) {
        if(head == null) {
            return; 
        }

        ListNode curr = head;
        ArrayList<ListNode> nodes = new ArrayList<ListNode>();

        nodes.add(curr); 

        while(curr.next != null) {
            curr = curr.next;
            nodes.add(curr); 
        }
    
        ListNode prev = null;

        for(int i = 0; i < nodes.size() / 2; i++) {
            if(nodes.get(i).next != null) {
                prev = nodes.get(i).next;
            }

            nodes.get(i).next = nodes.get(nodes.size() - 1 - i);

            if(prev != null) {
                nodes.get(nodes.size() - 1 - i).next = prev;
            }
            else {
                nodes.get(nodes.size() - 1 - i).next = null;
            }
        }

        nodes.get(nodes.size() / 2).next = null;
    }

    public ListNode helper() {
        ListNode e = new ListNode(5);
        ListNode d = new ListNode(4, e);
        ListNode c = new ListNode(3, d);
        ListNode b = new ListNode(2, c);
        ListNode a = new ListNode(1, b);

        new DailyChallenge082020().reorderList(a);

        return a;
    }

    public static void main(String[] args) {
        ListNode tmp = new DailyChallenge082020().helper();

        System.out.println(tmp.val);
        while(tmp.next != null) {
            tmp = tmp.next;
            System.out.println(tmp.val);
        }
    }
}
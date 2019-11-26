/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
        var num1 = ""
        var num2 = ""
        
        var t1 = l1
        var t2 = l2
        
        while(t1 != null || t2 != null) {
            if(t1 != null) {
                num1 = num1 + t1.`val`
                t1 = t1.next
            }
            
            if(t2 != null) {
                num2 = num2 + t2.`val`
                t2 = t2.next
            }
        }
        
        num1 = num1.reversed()
        num2 = num2.reversed()
        
        var sum = "${num1.toBigInteger() + num2.toBigInteger()}"
        
        var root: ListNode? = null
        var curr: ListNode? = null
        
        for(i in sum.length-1 downTo 0) {
            if(root == null) {
                root = ListNode(sum.substring(i..i).toInt())
            }
            else if(root.next == null) {
                root!!.next = ListNode(sum.substring(i..i).toInt())
                curr = root!!.next
            }
            else {
                curr!!.next = ListNode(sum.substring(i..i).toInt())
                curr = curr!!.next
            }
        }
        
        return root
    }
}

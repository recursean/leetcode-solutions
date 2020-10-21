public class DailyChallenge082420 {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public int sumOfLeftLeaves(TreeNode root) {
        printInorder(root);
    }

    public void printInorder(TreeNode node) { 
        if (node == null) 
            return; 
  
        /* first recur on left child */
        printInorder(node.left); 
  
        /* then print the data of node */
        System.out.print(node.val + " "); 
  
        /* now recur on right child */
        printInorder(node.right); 
    } 

    public int helper() {
        TreeNode d = new TreeNode(15);
        TreeNode e = new TreeNode(7);
        TreeNode b = new TreeNode(9);
        TreeNode c = new TreeNode(20, d, e);
        TreeNode a = new TreeNode(3, b, c);

        return new DailyChallenge082420().sumOfLeftLeaves(a);
    }

    public static void main(String[] args) {
        System.out.println(helper());
    }
}
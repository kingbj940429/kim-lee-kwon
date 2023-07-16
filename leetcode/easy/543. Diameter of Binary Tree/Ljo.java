package leetcode.easy;

public class Ljo {

    static class TreeNode {

        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    private int maxValue = -1;


    public int diameterOfBinaryTree(TreeNode root) {
        dist(root);
        return maxValue;
    }

    private int dist(TreeNode node) {
        if (node == null) {
            return -1;
        }
        var left = 1 + dist(node.left);
        var right = 1 + dist(node.right);
        maxValue = Math.max(maxValue, left + right);
        return Math.max(left, right);
    }

}

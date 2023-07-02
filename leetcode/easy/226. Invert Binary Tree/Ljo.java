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

    public TreeNode invertTree(TreeNode root) {
        invert(root);
        return root;
    }

    private void invert(TreeNode now) {
        if(now == null || (now.right == null && now.left == null)) {
            return;
        }
        invert(now.right);
        invert(now.left);
        var temp = now.right;
        now.right = now.left;
        now.left = temp;
    }

    // https://leetcode.com/problems/invert-binary-tree/solutions/
//    public TreeNode invertTree(TreeNode root) {
//        if (root != null) {
//            TreeNode temp = root.right;
//            root.right = root.left;
//            root.left = temp;
//            invertTree(root.right);
//            invertTree(root.left);
//        }
//        return root;
//    }

}

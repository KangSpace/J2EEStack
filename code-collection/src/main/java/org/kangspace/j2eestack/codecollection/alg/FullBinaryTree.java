package org.kangspace.j2eestack.codecollection.alg;

/**
 * @author kango2gler@gmail.com
 * @date 2024/6/27
 * @since
 */
public class FullBinaryTree {
    /*
    满二叉树证明
    写一个方法，入参是二叉树的根节点，返回boolean，如果是满二叉树返回true，不是返回false。
    public class TreeNode{
    private TreeNode left;
    private TreeNode right;
    private int val;
    }
    满二叉树:所有的叶子节点在同一层,所有的非叶子节点都有左右子节点
     */

    public class TreeNode {
        private TreeNode left;
        private TreeNode right;
        private int val;

        public TreeNode() {
        }

        public TreeNode(int val) {
            this.val = val;
        }

        public TreeNode(TreeNode left, TreeNode right, int val) {
            this.left = left;
            this.right = right;
            this.val = val;
        }

        public TreeNode getLeft() {
            return left;
        }

        public void setLeft(TreeNode left) {
            this.left = left;
        }

        public TreeNode getRight() {
            return right;
        }

        public void setRight(TreeNode right) {
            this.right = right;
        }

        public int getVal() {
            return val;
        }

        public void setVal(int val) {
            this.val = val;
        }
    }

    public boolean isFullBinaryTree(TreeNode root) {
        if (root == null) {
            return true; // 空树被认为是满二叉树
        }

        int depth = findDepth(root);
        return checkFullBinaryTree(root, depth, 0);
    }

    private boolean checkFullBinaryTree(TreeNode node, int depth, int level) {
        if (node == null) {
            return true;
        }

        // 如果是叶子节点，检查它是否在同一层
        if (node.getLeft() == null && node.getRight() == null) {
            return depth == level + 1;
        }

        // 如果是非叶子节点，检查它是否有左右子节点
        if (node.getLeft() == null || node.getRight() == null) {
            return false;
        }

        return checkFullBinaryTree(node.getLeft(), depth, level + 1) &&
                checkFullBinaryTree(node.getRight(), depth, level + 1);
    }

    private int findDepth(TreeNode node) {
        int depth = 0;
        while (node != null) {
            depth++;
            node = node.getLeft();
        }
        return depth;
    }

    public void test() {
        TreeNode root = new TreeNode(1);
        root.setLeft(new TreeNode(2));
        root.setRight(new TreeNode(3));
        root.getLeft().setLeft(new TreeNode(4));
        root.getLeft().setRight(new TreeNode(5));
        root.getRight().setLeft(new TreeNode(6));
        root.getRight().setRight(new TreeNode(7));

        System.out.println(isFullBinaryTree(root)); // 应该输出 true
    }

    public static void main(String[] args) {
        new FullBinaryTree().test();
    }
}

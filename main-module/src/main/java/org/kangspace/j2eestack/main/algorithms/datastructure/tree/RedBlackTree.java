package org.kangspace.j2eestack.main.algorithms.datastructure.tree;

import lombok.Data;
import lombok.Getter;
import lombok.Setter;

/**
 * 红黑树:
 * 性质1：每个节点要么是黑色，要么是红色。
 * 性质2：根节点是黑色。
 * 性质3：每个叶子节点（NIL）是黑色。
 * 性质4：从根节点到叶子节点任何一条路径上 不能出现两个连续的红结点
 * 性质5：从根节点到叶子节点任何一条路径上都包含数量相同的黑结点。
 *
 *
 * 红黑树能自平衡，需要三种操作：左旋、右旋和变色。
 * 左旋：以某个结点作为支点(旋转结点)，其右子结点变为旋转结点的父结点，右子结点的左子结点变为旋转结点的右子结点，左子结点保持不变。
 * 右旋：以某个结点作为支点(旋转结点)，其左子结点变为旋转结点的父结点，左子结点的右子结点变为旋转结点的左子结点，右子结点保持不变。
 * 变色：结点的颜色由红变黑或由黑变红。
 * @author kango2gler@gmail.com
 * @date 2024/3/18
 * @since
 */
@Getter
@Setter
public class RedBlackTree {

    public static boolean RED = true;
    public static boolean BLACK = false;

    Node root;

    public void insert(int val) {
        root = insert(root, val);
        root.color = BLACK;
    }

    public Node insert(Node node, int val) {
        if (node == null) {
            return new Node(val, RED);
        }
        if (val < node.data) {
            node.left = insert(node.left, val);
        }else if (val > node.data) {
            node.right = insert(node.right, val);
        }
        if (node.left.color == RED && node.right.color == RED) {

        }
        return node;
    }


    /**
     * 红黑树结点
     */
    public static class Node{
        private Node left;
        private Node right;
        private Node parent;
        private boolean color;
        private int data;

        public Node(int data, boolean color) {
            this.data = data;
            this.color = color;
        }
        public Node(int data) {
            this.data = data;
            this.color = RED;
        }
    }

}

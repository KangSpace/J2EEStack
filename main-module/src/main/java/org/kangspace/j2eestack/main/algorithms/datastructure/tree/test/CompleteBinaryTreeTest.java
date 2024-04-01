package org.kangspace.j2eestack.main.algorithms.datastructure.tree.test;

import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.LinkedList;
import java.util.Objects;
import java.util.Queue;

/**
 * 完全二叉树(基于链表实现)
 *
 * @author kango2gler@gmail.com
 * @date 2024/3/18
 * @since
 */
public class CompleteBinaryTreeTest {


    @Data
    @NoArgsConstructor
    public static class CompleteBinaryTree {
        private TreeNode root;
        private int size;

        public TreeNode insert(int i) {
            TreeNode newNode = new TreeNode(i);
            if (root == null) {
                root = newNode;
                size++;
                return root;
            }
            Queue<TreeNode> queue = new LinkedList<>();
            queue.add(root);
            while (!queue.isEmpty()) {
                TreeNode current = queue.poll();
                if (current.data == i) {
                    return current;
                }
                if (current.left == null) {
                    current.left = newNode;
                    break;
                } else {
                    queue.add(current.left);
                }
                if (current.right == null) {
                    current.right = newNode;
                    break;
                } else {
                    queue.add(current.right);
                }
            }
            size++;
            return newNode;
        }

        /**
         * 1. 找到最后一个节点和需要删除的节点替换
         * 2. 删除最后一个节点
         */
        public void delete(int i) {
            if (root == null) {
                return;
            }
            if (root.left == null && root.right == null) {
                if (root.data == i) {
                    root = null;
                }
                return;
            }
            Queue<TreeNode> queue = new LinkedList<>();
            queue.add(root);
            TreeNode keyNode = null, current;
            while (!queue.isEmpty()) {
                current = queue.poll();
                if (current.data == i) {
                    keyNode = current;
                    break;
                }
                if (current.left != null) {
                    queue.add(current.left);
                }
                if (current.right != null) {
                    queue.add(current.right);
                }
            }
            // 找到当前值
            if (keyNode != null) {
                // 找最后一个节点
                TreeNode lastNodeData = getLastNode();
                // 替换keyNode值为最后一个节点值
                keyNode.data = lastNodeData.data;
                // 删除最后一个节点
                deleteLastNode(lastNodeData);
                size--;
            }
        }

        public TreeNode getLastNode() {
            Queue<TreeNode> queue = new LinkedList<>();
            queue.add(root);
            TreeNode current = null;
            while (!queue.isEmpty()) {
                current = queue.poll();
                if (current.left != null) {
                    queue.add(current.left);
                }
                if (current.right != null) {
                    queue.add(current.right);
                }
            }
            return current;
        }

        public void deleteLastNode(TreeNode data) {
            Queue<TreeNode> queue = new LinkedList<>();
            queue.add(root);
            TreeNode current = null;
            while (!queue.isEmpty()) {
                current = queue.poll();
                if (current.left != null) {
                    if (Objects.equals(current.left, data)) {
                        current.left = null;
                        return;
                    } else {
                        queue.add(current.left);
                    }
                }
                if (current.right != null) {
                    if (Objects.equals(current.right, data)) {
                        current.right = null;
                        return;
                    } else {
                        queue.add(current.right);
                    }
                }
            }
        }

        public void levelOrderIterator() {
            Queue<TreeNode> queue = new LinkedList<>();
            queue.add(root);
            queue.add(null);
            while (!queue.isEmpty()) {
                TreeNode node = queue.poll();
                if (node == null) {
                    System.out.println("");
                    if (!queue.isEmpty()) {
                        queue.add(null);
                    }
                } else {
                    System.out.print(node.data + " ");
                    if (node.left != null) {
                        queue.add(node.left);
                    }
                    if (node.right != null) {
                        queue.add(node.right);
                    }
                }
            }
            System.out.println("");
        }
    }

    @Data
    public static class TreeNode {
        private TreeNode left;
        private TreeNode right;
        private int data;

        public TreeNode(int data) {
            this.data = data;
        }

        public TreeNode() {
        }
    }


    public static void main(String[] args) {
        CompleteBinaryTree completeBinaryTree = new CompleteBinaryTree();
        completeBinaryTree.insert(8);
        completeBinaryTree.insert(4);
        completeBinaryTree.insert(2);
        completeBinaryTree.insert(5);
        completeBinaryTree.insert(3);
        completeBinaryTree.insert(9);
        completeBinaryTree.insert(7);
        completeBinaryTree.insert(10);
        completeBinaryTree.insert(1);
        completeBinaryTree.levelOrderIterator();
        System.out.println("-------------------");
        completeBinaryTree.delete(8);
        completeBinaryTree.levelOrderIterator();
        System.out.println("-------------------");
        completeBinaryTree.delete(5);
        completeBinaryTree.levelOrderIterator();
    }
}

# 树的工具类
from queue import Queue


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


def inorder_traversal(root):
    """中序遍历"""
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.value)
    inorder_traversal(root.right)


def preorder_traversal(root):
    """前序遍历"""
    if root is None:
        return
    print(root.value)
    preorder_traversal(root.left)
    preorder_traversal(root.right)


def postorder_traversal(root):
    """后序遍历"""
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.value)


def level_order_traversal(root) -> None:
    """层序遍历"""
    if root is None:
        return
    queue = Queue()
    queue.put(root)
    while not queue.empty():
        node = queue.get()
        print(node.value)
        if node.left is not None:
            queue.put(node.left)
            print("/", end="")

        if node.right is not None:
            queue.put(node.right)
            print("\\")


def tree_height(root):
    """树的高度"""
    if root is None:
        return 0
    return max(tree_height(root.left), tree_height(root.right)) + 1

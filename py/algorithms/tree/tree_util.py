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
    print("level_order_traversal:(队列)")
    if root is None:
        return
    queue = Queue()
    queue.put(root)
    while not queue.empty():
        node = queue.get()
        print(node.value)
        if node.left is not None:
            queue.put(node.left)

        if node.right is not None:
            queue.put(node.right)


def level_order_traversal_2(root, is_root=True) -> None:
    """层序遍历"""
    if is_root:
        print("level_order_traversal_2:(递归)")
    if root is None:
        return
    print(root.value)
    if root.left is not None:
        level_order_traversal_2(root.left, False)

    if root.right is not None:
        level_order_traversal_2(root.right, False)


def print_tree_structure(root, prefix="", is_left=True, is_root=False):
    """
    打印树型结构
    Args:
        root: 根节点
        prefix: 前缀字符串，用于缩进
        is_left: 是否为左子节点
    """
    if is_root:
        print("print_tree_structure:")
    if root is None:
        return

    # 打印当前节点
    print(prefix + ("└── " if is_left else "┌── ") + str(root.value))

    # 计算新的前缀
    new_prefix = prefix + ("    " if is_left else "│   ")

    # 递归打印左右子树
    if root.right is not None:
        print_tree_structure(root.right, new_prefix, False)
    if root.left is not None:
        print_tree_structure(root.left, new_prefix, True)


def tree_height(root):
    """树的高度"""
    if root is None:
        return 0
    return max(tree_height(root.left), tree_height(root.right)) + 1


def create_sample_tree():
    """创建一个示例树用于测试"""
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    return root


# 测试代码
if __name__ == "__main__":
    # 创建示例树
    tree = create_sample_tree()

    print("=== 树型结构打印 ===")
    print("垂直结构:")
    print_tree_structure(tree)

    print("\n垂直结构（更清晰）:")
    print_tree_vertical(tree)

    print("\n水平结构:")
    print_tree_horizontal(tree)

    print("\n=== 遍历结果 ===")
    print("中序遍历:")
    inorder_traversal(tree)

    print("\n前序遍历:")
    preorder_traversal(tree)

    print("\n后序遍历:")
    postorder_traversal(tree)

    print("\n层序遍历:")
    level_order_traversal(tree)

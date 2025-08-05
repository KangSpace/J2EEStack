# -*- coding: utf-8 -*-
"""
红黑树删除方法测试脚本
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 由于文件名包含连字符，需要特殊处理
import importlib.util

spec = importlib.util.spec_from_file_location("red_black_tree", "red-black-tree.py")
red_black_tree = importlib.util.module_from_spec(spec)
spec.loader.exec_module(red_black_tree)
RedBlackTree = red_black_tree.RedBlackTree


def test_delete_leaf_node():
    """测试删除叶子节点"""
    print("=== 测试删除叶子节点 ===")
    rb_tree = RedBlackTree()

    # 插入节点
    values = [10, 5, 15, 3, 7, 12, 18]
    for value in values:
        rb_tree.insert(value)

    print("删除前的树:")
    rb_tree.print()
    print()

    # 删除叶子节点
    test_deletes = [3, 7, 12, 18]
    for value in test_deletes:
        print(f"删除节点 {value}:")
        rb_tree.delete_by_value(value)
        rb_tree.print()
        print()


def test_delete_node_with_one_child():
    """测试删除只有一个子节点的节点"""
    print("=== 测试删除只有一个子节点的节点 ===")
    rb_tree = RedBlackTree()

    # 构建特定场景
    values = [10, 5, 15, 3, 7, 12, 18, 2, 4, 6, 8, 11, 13, 16, 19]
    for value in values:
        rb_tree.insert(value)

    print("删除前的树:")
    rb_tree.print()
    print()

    # 删除只有一个子节点的节点
    test_deletes = [2, 4, 6, 8, 11, 13, 16, 19]
    for value in test_deletes:
        print(f"删除节点 {value}:")
        rb_tree.delete_by_value(value)
        rb_tree.print()
        print()


def test_delete_node_with_two_children():
    """测试删除有两个子节点的节点"""
    print("=== 测试删除有两个子节点的节点 ===")
    rb_tree = RedBlackTree()

    # 构建特定场景
    values = [10, 5, 15, 3, 7, 12, 18, 2, 4, 6, 8, 11, 13, 16, 19]
    for value in values:
        rb_tree.insert(value)

    print("删除前的树:")
    rb_tree.print()
    print()

    # 删除有两个子节点的节点
    test_deletes = [5, 15, 10]
    for value in test_deletes:
        print(f"删除节点 {value}:")
        rb_tree.delete_by_value(value)
        rb_tree.print()
        print()


def test_delete_root():
    """测试删除根节点"""
    print("=== 测试删除根节点 ===")
    rb_tree = RedBlackTree()

    # 插入节点
    values = [10, 5, 15, 3, 7, 12, 18]
    for value in values:
        rb_tree.insert(value)

    print("删除前的树:")
    rb_tree.print()
    print()

    print("删除根节点 10:")
    rb_tree.delete_by_value(10)
    rb_tree.print()
    print()


def test_delete_double_black_cases():
    """测试双黑情况"""
    print("=== 测试双黑情况 ===")
    rb_tree = RedBlackTree()

    # 构建会产生双黑情况的树
    values = [10, 5, 15, 3, 7, 12, 18, 2, 4, 6, 8, 11, 13, 16, 19]
    for value in values:
        rb_tree.insert(value)

    print("删除前的树:")
    rb_tree.print()
    print()

    # 删除会导致双黑情况的节点
    test_deletes = [3, 7, 12, 18]  # 这些是黑色叶子节点
    for value in test_deletes:
        print(f"删除节点 {value} (可能导致双黑):")
        rb_tree.delete_by_value(value)
        rb_tree.print()
        print()


def test_delete_nonexistent_node():
    """测试删除不存在的节点"""
    print("=== 测试删除不存在的节点 ===")
    rb_tree = RedBlackTree()

    # 插入节点
    values = [10, 5, 15, 3, 7, 12, 18]
    for value in values:
        rb_tree.insert(value)

    print("删除前的树:")
    rb_tree.print()
    print()

    # 删除不存在的节点
    test_deletes = [1, 9, 20, 100]
    for value in test_deletes:
        print(f"尝试删除不存在的节点 {value}:")
        rb_tree.delete_by_value(value)
        rb_tree.print()
        print()


def test_delete_all_nodes():
    """测试删除所有节点"""
    print("=== 测试删除所有节点 ===")
    rb_tree = RedBlackTree()

    # 插入节点
    values = [10, 5, 15, 3, 7, 12, 18]
    for value in values:
        rb_tree.insert(value)

    print("删除前的树:")
    rb_tree.print()
    print()

    # 逐个删除所有节点
    for value in values:
        print(f"删除节点 {value}:")
        rb_tree.delete_by_value(value)
        if rb_tree.root is not None:
            rb_tree.print()
        else:
            print("树为空")
        print()


def main():
    """主函数"""
    print("红黑树删除方法测试开始\n")

    test_delete_leaf_node()
    test_delete_node_with_one_child()
    test_delete_node_with_two_children()
    test_delete_root()
    test_delete_double_black_cases()
    test_delete_nonexistent_node()
    test_delete_all_nodes()

    print("红黑树删除方法测试完成")


if __name__ == "__main__":
    main()

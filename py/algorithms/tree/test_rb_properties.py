# -*- coding: utf-8 -*-
"""
红黑树性质验证测试脚本
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


def check_rb_properties(node, path_black_count, is_root=True):
    """
    递归检查红黑树性质
    
    Args:
        node: 当前节点
        path_black_count: 从根到当前路径的黑色节点数
        is_root: 是否为根节点
    
    Returns:
        (is_valid, black_count): 是否有效和黑色节点数
    """
    if node is None:
        return True, path_black_count
    
    # 性质1: 根节点是黑色
    if is_root and node.red:
        print(f"违反性质1: 根节点 {node.value} 是红色")
        return False, path_black_count
    
    # 性质4: 红色节点的子节点都是黑色
    if node.red:
        if node.left and node.left.red:
            print(f"违反性质4: 红色节点 {node.value} 的左子节点 {node.left.value} 也是红色")
            return False, path_black_count
        if node.right and node.right.red:
            print(f"违反性质4: 红色节点 {node.value} 的右子节点 {node.right.value} 也是红色")
            return False, path_black_count
    
    # 更新黑色节点计数
    current_black_count = path_black_count + (0 if node.red else 1)
    
    # 递归检查左右子树
    left_valid, left_black_count = check_rb_properties(node.left, current_black_count, False)
    right_valid, right_black_count = check_rb_properties(node.right, current_black_count, False)
    
    # 性质5: 所有路径的黑色节点数相同
    if left_black_count != right_black_count:
        print(f"违反性质5: 节点 {node.value} 的左右子树黑色节点数不同 (左:{left_black_count}, 右:{right_black_count})")
        return False, left_black_count
    
    return left_valid and right_valid, left_black_count


def validate_rb_tree(tree):
    """验证红黑树的所有性质"""
    if tree.root is None:
        print("树为空")
        return True
    
    print(f"验证红黑树性质...")
    is_valid, _ = check_rb_properties(tree.root, 0)
    
    if is_valid:
        print("✓ 所有红黑树性质都得到保持")
    else:
        print("✗ 红黑树性质被违反")
    
    return is_valid


def test_delete_with_validation():
    """测试删除操作并验证红黑树性质"""
    print("=== 测试删除操作并验证红黑树性质 ===")
    
    # 构建一个复杂的红黑树
    rb_tree = RedBlackTree()
    values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
    
    print("插入节点...")
    for value in values:
        rb_tree.insert(value)
        print(f"插入 {value}")
    
    print("\n初始树结构:")
    rb_tree.print()
    validate_rb_tree(rb_tree)
    print()
    
    # 测试删除操作
    test_deletes = [20, 40, 60, 80, 30, 70, 50]
    
    for value in test_deletes:
        print(f"\n删除节点 {value}:")
        rb_tree.delete_by_value(value)
        rb_tree.print()
        if not validate_rb_tree(rb_tree):
            print(f"删除节点 {value} 后红黑树性质被违反!")
            return False
        print()
    
    print("✓ 所有删除操作都保持了红黑树性质")
    return True


def test_edge_cases():
    """测试边界情况"""
    print("=== 测试边界情况 ===")
    
    # 测试空树删除
    rb_tree = RedBlackTree()
    print("测试空树删除:")
    rb_tree.delete_by_value(10)
    validate_rb_tree(rb_tree)
    print()
    
    # 测试单节点树删除
    rb_tree = RedBlackTree()
    rb_tree.insert(10)
    print("测试单节点树删除:")
    rb_tree.print()
    validate_rb_tree(rb_tree)
    rb_tree.delete_by_value(10)
    print("删除后:")
    validate_rb_tree(rb_tree)
    print()
    
    # 测试删除不存在的节点
    rb_tree = RedBlackTree()
    values = [10, 5, 15, 3, 7, 12, 18]
    for value in values:
        rb_tree.insert(value)
    
    print("测试删除不存在的节点:")
    rb_tree.print()
    validate_rb_tree(rb_tree)
    rb_tree.delete_by_value(100)
    print("删除不存在的节点100后:")
    validate_rb_tree(rb_tree)
    print()


def test_double_black_scenarios():
    """测试双黑情况"""
    print("=== 测试双黑情况 ===")
    
    # 构建会产生双黑情况的树
    rb_tree = RedBlackTree()
    values = [10, 5, 15, 3, 7, 12, 18, 2, 4, 6, 8, 11, 13, 16, 19]
    
    print("构建测试树...")
    for value in values:
        rb_tree.insert(value)
    
    print("初始树结构:")
    rb_tree.print()
    validate_rb_tree(rb_tree)
    print()
    
    # 删除会导致双黑情况的黑色节点
    black_leaf_nodes = [3, 7, 12, 18]  # 这些是黑色叶子节点
    
    for value in black_leaf_nodes:
        print(f"删除黑色叶子节点 {value} (可能导致双黑):")
        rb_tree.delete_by_value(value)
        rb_tree.print()
        if not validate_rb_tree(rb_tree):
            print(f"删除节点 {value} 后红黑树性质被违反!")
            return False
        print()
    
    print("✓ 所有双黑情况都正确处理")
    return True


def main():
    """主函数"""
    print("红黑树性质验证测试开始\n")
    
    success = True
    
    try:
        success &= test_delete_with_validation()
        test_edge_cases()
        success &= test_double_black_scenarios()
    except Exception as e:
        print(f"测试过程中发生错误: {e}")
        success = False
    
    if success:
        print("\n✓ 所有测试通过，delete方法实现正确")
    else:
        print("\n✗ 测试失败，delete方法存在问题")
    
    print("红黑树性质验证测试完成")


if __name__ == "__main__":
    main() 
# -*- coding: utf-8 -*-
"""
全面的红黑树删除测试
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
    """检查红黑树性质"""
    if node is None:
        return True, path_black_count
    
    # 性质1: 根节点是黑色
    if is_root and node.red:
        return False, path_black_count
    
    # 性质4: 红色节点的子节点都是黑色
    if node.red:
        if node.left and node.left.red:
            return False, path_black_count
        if node.right and node.right.red:
            return False, path_black_count
    
    # 更新黑色节点计数
    current_black_count = path_black_count + (0 if node.red else 1)
    
    # 递归检查左右子树
    left_valid, left_black_count = check_rb_properties(node.left, current_black_count, False)
    right_valid, right_black_count = check_rb_properties(node.right, current_black_count, False)
    
    # 性质5: 所有路径的黑色节点数相同
    if left_black_count != right_black_count:
        return False, left_black_count
    
    return left_valid and right_valid, left_black_count


def validate_rb_tree(tree):
    """验证红黑树的所有性质"""
    if tree.root is None:
        return True
    
    is_valid, _ = check_rb_properties(tree.root, 0)
    return is_valid


def test_comprehensive_deletion():
    """全面的删除测试"""
    print("=== 全面删除测试 ===")
    
    # 测试用例1: 删除所有节点
    print("测试用例1: 删除所有节点")
    rb_tree = RedBlackTree()
    values = [10, 5, 15, 3, 7, 12, 18]
    for value in values:
        rb_tree.insert(value)
    
    print("初始树:")
    rb_tree.print()
    assert validate_rb_tree(rb_tree), "初始树违反红黑树性质"
    
    # 逐个删除所有节点
    for value in values:
        print(f"\n删除节点 {value}:")
        rb_tree.delete_by_value(value)
        if rb_tree.root is not None:
            rb_tree.print()
        else:
            print("树为空")
        assert validate_rb_tree(rb_tree), f"删除节点 {value} 后违反红黑树性质"
    
    print("✓ 测试用例1通过")
    
    # 测试用例2: 删除根节点
    print("\n测试用例2: 删除根节点")
    rb_tree = RedBlackTree()
    values = [10, 5, 15, 3, 7, 12, 18]
    for value in values:
        rb_tree.insert(value)
    
    print("初始树:")
    rb_tree.print()
    assert validate_rb_tree(rb_tree), "初始树违反红黑树性质"
    
    # 删除根节点
    root_value = rb_tree.root.value
    print(f"\n删除根节点 {root_value}:")
    rb_tree.delete_by_value(root_value)
    rb_tree.print()
    assert validate_rb_tree(rb_tree), "删除根节点后违反红黑树性质"
    
    print("✓ 测试用例2通过")
    
    # 测试用例3: 删除黑色叶子节点（双黑情况）
    print("\n测试用例3: 删除黑色叶子节点")
    rb_tree = RedBlackTree()
    values = [10, 5, 15, 3, 7, 12, 18, 2, 4, 6, 8, 11, 13, 16, 19]
    for value in values:
        rb_tree.insert(value)
    
    print("初始树:")
    rb_tree.print()
    assert validate_rb_tree(rb_tree), "初始树违反红黑树性质"
    
    # 删除黑色叶子节点
    black_leaf_nodes = [3, 7, 12, 18]
    for value in black_leaf_nodes:
        print(f"\n删除黑色叶子节点 {value}:")
        rb_tree.delete_by_value(value)
        rb_tree.print()
        assert validate_rb_tree(rb_tree), f"删除黑色叶子节点 {value} 后违反红黑树性质"
    
    print("✓ 测试用例3通过")
    
    # 测试用例4: 删除有两个子节点的节点
    print("\n测试用例4: 删除有两个子节点的节点")
    rb_tree = RedBlackTree()
    values = [10, 5, 15, 3, 7, 12, 18, 2, 4, 6, 8, 11, 13, 16, 19]
    for value in values:
        rb_tree.insert(value)
    
    print("初始树:")
    rb_tree.print()
    assert validate_rb_tree(rb_tree), "初始树违反红黑树性质"
    
    # 删除有两个子节点的节点
    two_child_nodes = [5, 15, 10]
    for value in two_child_nodes:
        print(f"\n删除有两个子节点的节点 {value}:")
        rb_tree.delete_by_value(value)
        rb_tree.print()
        assert validate_rb_tree(rb_tree), f"删除有两个子节点的节点 {value} 后违反红黑树性质"
    
    print("✓ 测试用例4通过")
    
    # 测试用例5: 删除只有一个子节点的节点
    print("\n测试用例5: 删除只有一个子节点的节点")
    rb_tree = RedBlackTree()
    values = [10, 5, 15, 3, 7, 12, 18, 2, 4, 6, 8, 11, 13, 16, 19]
    for value in values:
        rb_tree.insert(value)
    
    print("初始树:")
    rb_tree.print()
    assert validate_rb_tree(rb_tree), "初始树违反红黑树性质"
    
    # 删除只有一个子节点的节点
    one_child_nodes = [2, 4, 6, 8, 11, 13, 16, 19]
    for value in one_child_nodes:
        print(f"\n删除只有一个子节点的节点 {value}:")
        rb_tree.delete_by_value(value)
        rb_tree.print()
        assert validate_rb_tree(rb_tree), f"删除只有一个子节点的节点 {value} 后违反红黑树性质"
    
    print("✓ 测试用例5通过")
    
    # 测试用例6: 删除不存在的节点
    print("\n测试用例6: 删除不存在的节点")
    rb_tree = RedBlackTree()
    values = [10, 5, 15, 3, 7, 12, 18]
    for value in values:
        rb_tree.insert(value)
    
    print("初始树:")
    rb_tree.print()
    assert validate_rb_tree(rb_tree), "初始树违反红黑树性质"
    
    # 删除不存在的节点
    nonexistent_nodes = [1, 9, 20, 100]
    for value in nonexistent_nodes:
        print(f"\n尝试删除不存在的节点 {value}:")
        rb_tree.delete_by_value(value)
        rb_tree.print()
        assert validate_rb_tree(rb_tree), f"尝试删除不存在的节点 {value} 后违反红黑树性质"
    
    print("✓ 测试用例6通过")
    
    # 测试用例7: 空树删除
    print("\n测试用例7: 空树删除")
    rb_tree = RedBlackTree()
    print("空树:")
    assert validate_rb_tree(rb_tree), "空树违反红黑树性质"
    
    # 尝试删除空树中的节点
    rb_tree.delete_by_value(10)
    assert validate_rb_tree(rb_tree), "空树删除后违反红黑树性质"
    print("✓ 测试用例7通过")
    
    # 测试用例8: 单节点树删除
    print("\n测试用例8: 单节点树删除")
    rb_tree = RedBlackTree()
    rb_tree.insert(10)
    
    print("单节点树:")
    rb_tree.print()
    assert validate_rb_tree(rb_tree), "单节点树违反红黑树性质"
    
    # 删除单节点
    rb_tree.delete_by_value(10)
    assert validate_rb_tree(rb_tree), "删除单节点后违反红黑树性质"
    print("✓ 测试用例8通过")
    
    # 测试用例9: 复杂场景
    print("\n测试用例9: 复杂场景")
    rb_tree = RedBlackTree()
    values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
    for value in values:
        rb_tree.insert(value)
    
    print("初始树:")
    rb_tree.print()
    assert validate_rb_tree(rb_tree), "初始树违反红黑树性质"
    
    # 复杂删除序列
    delete_sequence = [20, 40, 60, 80, 30, 70, 50, 10, 25, 35, 45, 55, 65, 75, 85]
    for value in delete_sequence:
        if rb_tree.search(value) is not None:  # 只删除存在的节点
            print(f"\n删除节点 {value}:")
            rb_tree.delete_by_value(value)
            if rb_tree.root is not None:
                rb_tree.print()
            else:
                print("树为空")
            assert validate_rb_tree(rb_tree), f"删除节点 {value} 后违反红黑树性质"
    
    print("✓ 测试用例9通过")
    
    print("\n✓ 所有测试用例通过！")


def test_edge_cases():
    """测试边界情况"""
    print("=== 边界情况测试 ===")
    
    # 测试1: 删除红色叶子节点
    print("测试1: 删除红色叶子节点")
    rb_tree = RedBlackTree()
    values = [10, 5, 15, 3, 7, 12, 18]
    for value in values:
        rb_tree.insert(value)
    
    # 找到红色叶子节点
    red_leaf_nodes = []
    def find_red_leaves(node):
        if node is None:
            return
        if node.left is None and node.right is None and node.red:
            red_leaf_nodes.append(node.value)
        find_red_leaves(node.left)
        find_red_leaves(node.right)
    
    find_red_leaves(rb_tree.root)
    print(f"红色叶子节点: {red_leaf_nodes}")
    
    for value in red_leaf_nodes:
        print(f"\n删除红色叶子节点 {value}:")
        rb_tree.delete_by_value(value)
        rb_tree.print()
        assert validate_rb_tree(rb_tree), f"删除红色叶子节点 {value} 后违反红黑树性质"
    
    print("✓ 测试1通过")
    
    # 测试2: 删除黑色内部节点
    print("\n测试2: 删除黑色内部节点")
    rb_tree = RedBlackTree()
    values = [10, 5, 15, 3, 7, 12, 18]
    for value in values:
        rb_tree.insert(value)
    
    # 找到黑色内部节点
    black_internal_nodes = []
    def find_black_internals(node):
        if node is None:
            return
        if not node.red and (node.left is not None or node.right is not None):
            black_internal_nodes.append(node.value)
        find_black_internals(node.left)
        find_black_internals(node.right)
    
    find_black_internals(rb_tree.root)
    print(f"黑色内部节点: {black_internal_nodes}")
    
    for value in black_internal_nodes:
        print(f"\n删除黑色内部节点 {value}:")
        rb_tree.delete_by_value(value)
        rb_tree.print()
        assert validate_rb_tree(rb_tree), f"删除黑色内部节点 {value} 后违反红黑树性质"
    
    print("✓ 测试2通过")
    
    print("\n✓ 所有边界情况测试通过！")


def main():
    """主函数"""
    print("全面红黑树删除测试开始\n")
    
    try:
        test_comprehensive_deletion()
        test_edge_cases()
        print("\n🎉 所有测试通过！delete方法实现正确")
    except AssertionError as e:
        print(f"\n❌ 测试失败: {e}")
    except Exception as e:
        print(f"\n❌ 测试过程中发生错误: {e}")
    
    print("\n全面红黑树删除测试完成")


if __name__ == "__main__":
    main() 
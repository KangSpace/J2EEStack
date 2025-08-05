# -*- coding: utf-8 -*-
"""
红黑树测试脚本
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


def test_basic_insertion():
    """测试基本插入功能"""
    print("=== 测试基本插入功能 ===")
    rb_tree = RedBlackTree()

    # 测试空树插入
    rb_tree.insert(10)
    print("插入10后:")
    rb_tree.print()
    print()

    # 测试多个节点插入
    values = [5, 15, 3, 7, 12, 18]
    for value in values:
        rb_tree.insert(value)
        print(f"插入{value}后:")
        rb_tree.print()
        print()


def test_ll_case():
    """测试LL Case (左-左情况)"""
    print("=== 测试LL Case ===")
    rb_tree = RedBlackTree()

    # 构建LL Case场景: 插入 30, 20, 10
    values = [30, 20, 10]
    for value in values:
        rb_tree.insert(value)
        print(f"插入{value}后:")
        rb_tree.print()
        print()


def test_rr_case():
    """测试RR Case (右-右情况)"""
    print("=== 测试RR Case ===")
    rb_tree = RedBlackTree()

    # 构建RR Case场景: 插入 10, 20, 30
    values = [10, 20, 30]
    for value in values:
        rb_tree.insert(value)
        print(f"插入{value}后:")
        rb_tree.print()
        print()


def test_lr_case():
    """测试LR Case (左-右情况)"""
    print("=== 测试LR Case ===")
    rb_tree = RedBlackTree()

    # 构建LR Case场景: 插入 30, 10, 20
    values = [30, 10, 20]
    for value in values:
        rb_tree.insert(value)
        print(f"插入{value}后:")
        rb_tree.print()
        print()


def test_rl_case():
    """测试RL Case (右-左情况)"""
    print("=== 测试RL Case ===")
    rb_tree = RedBlackTree()

    # 构建RL Case场景: 插入 10, 30, 20
    values = [10, 30, 20]
    for value in values:
        rb_tree.insert(value)
        print(f"插入{value}后:")
        rb_tree.print()
        print()


def test_uncle_red_case():
    """测试叔叔节点为红色的情况"""
    print("=== 测试叔叔节点为红色的情况 ===")
    rb_tree = RedBlackTree()

    # 构建叔叔节点为红色的场景
    values = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    for value in values:
        rb_tree.insert(value)
        print(f"插入{value}后:")
        rb_tree.print()
        print()


def test_complex_scenario():
    """测试复杂场景"""
    print("=== 测试复杂场景 ===")
    rb_tree = RedBlackTree()

    # 测试文档中提到的测试用例
    test_cases = [
        ([71, 85, 80, 88, 61, 65], "LR Case测试用例"),
        ([71, 85, 80, 88, 95], "RR Case测试用例"),
        ([71, 85, 80, 88, 95, 92, 100, 120, 110], "RL Case测试用例"),
    ]

    for values, description in test_cases:
        print(f"\n{description}: {values}")
        rb_tree = RedBlackTree()
        for value in values:
            rb_tree.insert(value)
        print("最终结果:")
        rb_tree.print()
        print()


def test_search():
    """测试查找功能"""
    print("=== 测试查找功能 ===")
    rb_tree = RedBlackTree()

    values = [10, 5, 15, 3, 7, 12, 18]
    for value in values:
        rb_tree.insert(value)

    print("树结构:")
    rb_tree.print()
    print()

    # 测试存在的值
    test_values = [10, 5, 15, 3, 7, 12, 18, 100]
    for value in test_values:
        result = rb_tree.search(value)
        if result:
            print(f"找到值 {value}: {result.value}({'R' if result.red else 'B'})")
        else:
            print(f"未找到值 {value}")


def main():
    """主函数"""
    print("红黑树测试开始\n")

    test_basic_insertion()
    test_ll_case()
    test_rr_case()
    test_lr_case()
    test_rl_case()
    test_uncle_red_case()
    test_complex_scenario()
    test_search()

    print("红黑树测试完成")


if __name__ == "__main__":
    main()

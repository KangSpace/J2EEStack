"""
前缀树(Trie),
又称为字典树或单词查找树，是一种树形数据结构，专门用于处理字符串集合。
它具有高效的字符串插入、查找和以某个前缀为起点的字符串集合查找操作。
前缀树特别适用于自动补全、拼写检查、词频统计等应用场景。

前缀树的结构:
    1. 每个节点包含一个字符
    2. 从根节点到叶子节点的路径表示一个字符串
    3. 每个节点可以有多个子节点

实现逻辑:
1. 使用Map实现
2. 使用数组实现
"""

from tree_util import TreeNode


class TrieNodeByMap:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

    def insert(self, word: str):
        root = self
        exists = True
        for char in word:
            if char not in (children := root.children):
                children[char] = TrieNodeByMap()
            else:
                root = children[char]
        else:
            root.is_end_of_word = True

    def search(self, word: str) -> bool:
        root = self
        for char in word:
            if char not in (children := root.children):
                return False
            root = children[char]
        return root.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        root = self
        for char in prefix:
            ...


class TrieNodeByArray:
    def __init__(self, value): ...


class TireTree:
    def __init__(self, by_map: bool = True):
        """
        Args:
            by_map (bool, optional): 使用Map实现. Defaults to True. false时使用数组
        """
        self.root = TrieNodeByMap() if by_map else TrieNodeByArray()

    def insert(self, word: str):
        node = self.root
        self.root.insert(word)

"""
前缀树(Trie),
又称为字典树或单词查找树，是一种树形数据结构，专门用于处理字符串集合。
它具有高效的字符串插入、查找和以某个前缀为起点的字符串集合查找操作。
前缀树特别适用于自动补全、拼写检查、词频统计等应用场景。

时间复杂度: O(m) 其中m是单词的长度, 插入,搜索,删除的平均时间复杂度为O(m)
节点保存: 是否是单词结尾, 子节点Map/列表
- 插入: 从root开始循环单词每个元素, 从单词开头扫描root, 如果子节点不存在, 则创建, 否则root变更为子节点继续在循环中迭代, 直到单词结尾, 设置is_end_of_word为True
```
def insert(self, word: str):
    root = self
    for char in word:
        if char not in root.children:
            root.children[char] = TrieNodeByMap()
        root = root.children[char]
    root.is_end_of_word = True
```
- 查询: 从root开始循环单词的每个元素, 从单词开头扫描root, 如果子节点不存在, 则返回False, 否则root变更为子节点继续在循环中迭代, 直到单词结尾, 返回is_end_of_word
```
def search(self, word: str) -> bool:
    root = self
    for char in word:
        if char not in (children := root.children):
            return False
        root = children[char]
    return root.is_end_of_word
```
- 查询前缀匹配: 1. 查询前缀开头的最后一个节点 2. 从最后一个节点开始递归, 定义一个list,和对应层的word, 收集所有is_end_of_word为True的word
```
def find_words_with_prefix(self, prefix: str) -> list[str]:
    node = self.find_node_with_prefix(prefix)
    if node is False:
        return []

    words = []
    self._collect_words_from_node(node, prefix, words)
    return words

def _collect_words_from_node(
    self, node: "TrieNodeByMap", current_word: str, words: list[str]
):
    # 递归收集从当前节点开始的所有单词
    if node.is_end_of_word:
        words.append(current_word)
    # 遍历每个子节点
    for child, node in node.children.items():
        self._collect_words_from_node(node, current_word + child, words)
```
- 删除: 1. 检查单词是否存在 2: 指定1个索引index, 从index=0开始, 到index==len(word)时检查是否是单词结尾, 如果是, 则设置is_end_of_word为False,如果无子节点,则返回True, 否则返回False
返回True时需要删除节点 (递归处理)
```
def delete(self, word: str) -> bool:
    if not word:
        return False

    # 先检查单词是否存在
    if not self.search(word):
        return False

    # 使用递归删除，这样可以清理无用的节点
    self._delete_recursive(self, word, 0)
    return True

def _delete_recursive(self, node: "TrieNodeByMap", word: str, index: int) -> bool:
    # 如果已经处理完所有字符
    if index == len(word):
        # 如果当前节点是单词结尾
        if node.is_end_of_word:
            node.is_end_of_word = False
            # 如果当前节点没有子节点，可以删除
            return len(node.children) == 0
        return False

    char = word[index]
    if char not in node.children:
        return False

    # 递归删除子节点
    should_delete_child = self._delete_recursive(
        node.children[char], word, index + 1
    )

    if should_delete_child:
        # 删除子节点
        del node.children[char]
        # 如果当前节点不是单词结尾且没有其他子节点，也可以删除
        return not node.is_end_of_word and len(node.children) == 0

    return False
```

前缀树的结构:
    1. 每个节点包含一个字符
    2. 从根节点到叶子节点的路径表示一个字符串
    3. 每个节点可以有多个子节点

实现逻辑:
1. 使用Map实现O(m)
2. 使用数组实现O(m^2)

map比数组实现简单, 查询速度更快, 但数组实现空间利用率更高
"""

from tree_util import TreeNode


class TrieNodeByMap:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

    def insert(self, word: str):
        root = self
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNodeByMap()
            root = root.children[char]
        root.is_end_of_word = True

    def search(self, word: str) -> bool:
        root = self
        for char in word:
            if char not in (children := root.children):
                return False
            root = children[char]
        return root.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        return self.find_node_with_prefix(prefix) is not None

    def find_node_with_prefix(self, prefix: str) -> "TrieNodeByMap":
        root = self
        for char in prefix:
            if char not in (children := root.children):
                return None
            root = children[char]
        return root

    def find_words_with_prefix(self, prefix: str) -> list[str]:
        node = self.find_node_with_prefix(prefix)
        if node is False:
            return []

        words = []
        self._collect_words_from_node(node, prefix, words)
        return words

    def _collect_words_from_node(
        self, node: "TrieNodeByMap", current_word: str, words: list[str]
    ):
        """递归收集从当前节点开始的所有单词"""
        if node.is_end_of_word:
            words.append(current_word)
        # 遍历每个子节点
        for child, node in node.children.items():
            self._collect_words_from_node(node, current_word + child, words)

    def delete(self, word: str) -> bool:
        """
        删除单词
        返回 True 如果单词存在且被删除，否则返回 False
        """
        if not word:
            return False

        # 先检查单词是否存在
        if not self.search(word):
            return False

        # 使用递归删除，这样可以清理无用的节点
        self._delete_recursive(self, word, 0)
        return True

    def _delete_recursive(self, node: "TrieNodeByMap", word: str, index: int) -> bool:
        """
        递归删除单词
        (
            反向处理逻辑, 先处理最后一层, 从后往前处理:
            1. 如果当前节点是单词结尾, 则设置is_end_of_word为False, 如果无子节点,则返回True, 否则返回False
            2. 判断word[index]是否在该层的children中存在, 不存在直接返回False
            3. 递归执行删除逻辑, node 变更为子节点, index + 1, 继续递归处理
            4. 判断递归结果(是否需要删除), 如果需要删除, 则删除子节点, 并判断当前层的node是否是结尾和是否有其他子节点, 如果无其他子节点, 则返回True, 否则返回False
            5. 返回False时, 说明不需要删除, 直接返回False
        )
        Args:
            node: 当前节点
            word: 要删除的单词
            index: 当前处理的字符索引
        Returns:
            True 如果应该删除当前节点，False 否则
        """
        # 如果已经处理完所有字符
        if index == len(word):
            # 如果当前节点是单词结尾
            if node.is_end_of_word:
                node.is_end_of_word = False
                # 如果当前节点没有子节点，可以删除
                return len(node.children) == 0
            return False

        char = word[index]
        if char not in node.children:
            return False

        # 递归删除子节点
        should_delete_child = self._delete_recursive(
            node.children[char], word, index + 1
        )

        if should_delete_child:
            # 删除子节点
            del node.children[char]
            # 如果当前节点不是单词结尾且没有其他子节点，也可以删除
            return not node.is_end_of_word and len(node.children) == 0

        return False


class TrieNodeByArray:
    def __init__(self, value=None):
        self.value = value
        self.children = []
        self.is_end_of_word = False

    def insert(self, word: str):
        root = self
        for chr in word:
            for child in root.children:
                if chr == child.value:
                    root = child
                    break
            else:
                new_node = TrieNodeByArray(chr)
                root.children.append(new_node)
                root = new_node

        root.is_end_of_word = True

    def search(self, word: str) -> bool:
        root = self
        for chr in word:
            for child in root.children:
                if chr == child.value:
                    root = child
                    break
            else:
                return False
        return root.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        return self.find_node_with_prefix(prefix) is not None

    def find_node_with_prefix(self, prefix: str) -> "TrieNodeByArray":
        root = self
        for chr in prefix:
            for child in root.children:
                if chr == child.value:
                    root = child
                    break
            else:
                return None
        return root

    def find_words_with_prefix(self, prefix: str) -> list[str]:
        node = self.find_node_with_prefix(prefix)
        if node is None:
            return []
        words = []
        self._collect_words_from_node(node, prefix, words)
        return words

    def _collect_words_from_node(
        self, node: "TrieNodeByArray", current_word: str, words: list[str]
    ):
        # 1. 先检查是否是单词结尾
        if node.is_end_of_word:
            words.append(current_word)
        # 2. 遍历每个子节点递归检查
        for child in node.children:
            self._collect_words_from_node(child, current_word + child.value, words)

    def delete(self, word: str) -> bool:
        # 1. 先判断是否存在
        if not word or not self.search(word):
            return False
        # 2. 递归删除每一层(从最后一层开始删,然后向上递归)
        return self._delete_recursive(self, word, 0)

    def _delete_recursive(self, node: "TrieNodeByArray", word: str, index: int) -> bool:
        # 1. 最后一层, 判断是否单词结尾
        if index == len(word):
            if node.is_end_of_word:
                node.is_end_of_word = False
                return len(node.children) == 0
            return False  # 非最后一层, 直接返回, 也表示单词不存在的情况
        # 2. 判断当前节点中是否存在单词的当前层字符
        chr = word[index]
        node_children = node.children
        next_node = None
        for child in node_children:
            if chr == child.value:
                next_node = child
                break
        else:
            return False
        # 3. 递归删除子节点
        should_delete_child = self._delete_recursive(next_node, word, index + 1)
        # 4. 判断是否需要删除子节点
        if should_delete_child:
            node_children.remove(next_node)
            return not node.is_end_of_word and len(node_children) == 0
        return False


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

    def print_tree(self, prefix: str = ""):
        words = self.root.find_words_with_prefix(prefix)
        print(words)


def test_trie_tree():
    """测试 Trie 树的各种功能"""
    print("=== Trie 树功能测试 ===")
    by_map = False
    print(f"实现方式: {'Map' if by_map else 'Array'}")

    # 创建 Trie 树
    trie = TireTree(by_map)

    # 测试数据
    test_words = [
        "apple",
        "app",
        "application",
        "apply",
        "applicant",
        "banana",
        "band",
        "bandit",
        "banish",
        "cat",
        "car",
        "card",
        "careful",
        "care",
        "dog",
        "door",
        "dormitory",
        "dorm",
        "elephant",
        "eleven",
        "elevator",
    ]

    print(f"插入单词: {test_words}")
    for word in test_words:
        trie.insert(word)

    print("\n=== 测试搜索功能 ===")
    search_tests = [
        ("apple", True),
        ("app", True),
        ("application", True),
        ("banana", True),
        ("cat", True),
        ("dog", True),
        ("elephant", True),
        ("xyz", False),
        ("appl", False),  # "appl" 不是完整单词，所以应该是 False
        ("banan", False),
    ]

    for word, expected in search_tests:
        result = trie.root.search(word)
        status = "✓" if result == expected else "✗"
        print(f"{status} 搜索 '{word}': 期望 {expected}, 实际 {result}")

    print("\n=== 测试前缀查找功能 ===")
    prefix_tests = [
        ("app", ["app", "apple", "application", "apply", "applicant"]),
        ("ban", ["banana", "band", "bandit", "banish"]),
        ("ca", ["cat", "car", "card", "careful", "care"]),
        ("do", ["dog", "door", "dormitory", "dorm"]),
        ("ele", ["elephant", "eleven", "elevator"]),
        ("xyz", []),
        ("", test_words),  # 空前缀返回所有单词
    ]

    for prefix, expected in prefix_tests:
        result = trie.root.find_words_with_prefix(prefix)
        result.sort()
        expected.sort()
        status = "✓" if result == expected else "✗"
        print(f"{status} 前缀 '{prefix}':")
        print(f"    期望: {expected}")
        print(f"    实际: {result}")

    print("\n=== 测试 starts_with 功能 ===")
    starts_with_tests = [
        ("app", True),
        ("ban", True),
        ("ca", True),
        ("do", True),
        ("ele", True),
        ("xyz", False),
        ("appl", True),  # "appl" 是 "apple" 和 "application" 的前缀
    ]

    for prefix, expected in starts_with_tests:
        result = trie.root.starts_with(prefix)
        status = "✓" if result == expected else "✗"
        print(f"{status} starts_with '{prefix}': 期望 {expected}, 实际 {result}")

    print("\n=== 测试 print_tree 功能 ===")
    print("所有单词:")
    trie.print_tree()

    print("\n以 'app' 开头的单词:")
    trie.print_tree("app")

    print("\n以 'ban' 开头的单词:")
    trie.print_tree("ban")

    print("\n=== 测试删除功能 ===")
    # 测试删除功能
    delete_tests = [
        ("apple", True),  # 删除存在的单词
        ("app", True),  # 删除存在的单词
        ("xyz", False),  # 删除不存在的单词
        ("banan", False),  # 删除不存在的单词
    ]

    for word, expected in delete_tests:
        result = trie.root.delete(word)
        status = "✓" if result == expected else "✗"
        print(f"{status} 删除 '{word}': 期望 {expected}, 实际 {result}")

    print("\n删除后的单词列表:")
    trie.print_tree()

    print("\n删除后以 'app' 开头的单词:")
    trie.print_tree("app")

    print("\n删除后以 'ban' 开头的单词:")
    trie.print_tree("ban")

    # 测试删除后搜索
    print("\n=== 测试删除后的搜索功能 ===")
    search_after_delete_tests = [
        ("apple", False),  # 已删除
        ("app", False),  # 已删除
        ("application", True),  # 仍然存在
        ("banana", True),  # 仍然存在
    ]

    for word, expected in search_after_delete_tests:
        result = trie.root.search(word)
        status = "✓" if result == expected else "✗"
        print(f"{status} 删除后搜索 '{word}': 期望 {expected}, 实际 {result}")

    print("\n=== 测试完成 ===")


if __name__ == "__main__":
    test_trie_tree()

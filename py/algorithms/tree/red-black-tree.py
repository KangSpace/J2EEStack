# -*- coding: utf-8 -*-


class Node:
    """A node in a red-black tree."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.red = True


class RedBlackTree:
    """A red-black tree.

    Reference:
    - 定义: https://www.geeksforgeeks.org/dsa/red-black-tree-definition-meaning-in-dsa/
    - 插入: https://www.geeksforgeeks.org/dsa/insertion-in-red-black-tree/
    - 删除: https://www.geeksforgeeks.org/dsa/deletion-in-red-black-tree/

    Visualization: https://www.cs.usfca.edu/~galles/visualization/RedBlack.html


    红黑树的定义：
    1. 节点是红色或黑色
    2. 根节点是黑色
    3. 所有叶子节点是黑色(一般叶子节点是NIL节点)
    4. 如果一个节点是红色，则它的两个子节点都是黑色(即,不能有2个相连的红色节点)
    5. 对每个节点，从该节点到其所有后代叶子节点的简单路径上，具有相同数量的黑色节点（黑色高度保持一致）。

    > 1. 新插入的节点是红色节点
    > 2. 红黑树是平衡二叉树

    重点:

    1. 着色和旋转

        1. 插入节点

           - 普通情况(根、父节点为黑色， 重新着色、直接插入)
           - 普通情况2(父节点、叔节点都为红色， 着色)
           - 处理双红节点冲突(4种情况， 旋转+着色)

        2. 删除节点

    常用方法:
    1. 插入节点
    1.1 左旋
    1.2 右旋
    2. 删除节点
    3. 查找节点
    """

    def __init__(self):
        self.root = None
        self.ll = False  # LL Case标记, 非执行左旋,实际是执行右旋. 有些代码会将这个字段表示为旋转方向
        self.lr = False  # LR Case标记
        self.rr = False  # RR Case标记
        self.rl = False  # RL Case标记

    def insert(self, value):
        """插入节点

        红黑树插入节点情况(2大类):

        > 新节点默认是红色的
        > x(R/B) 为新插入节点, R为红色, B为黑色

        **情况1: 插入的节点是根节点**

        > 此时树为单一节点, 设置新节点为根节点

           **处理**: 将其颜色设置为黑色

           **图例**:

            ```
            x(B)
            ```


        **情况2: 插入的节点是叶子节点(2大类)**


            **情况2.1: 父节点是黑色**

            > 此时, 因为新节点是红色, 可以满足【任意节点到叶子节点的路径上, 黑色节点数量相同， 即黑高保持一致, 且没有相邻的红色节点】


                **处理**: 直接插入新节点, 其他不变

                **图例**:


                ```
                R(B)
                / \\
                  x(B)  
                
                ```



            **情况2.2: 父节点是红色(2大类)**

            > 此时, 新节点的父节点是红色, 违反了红黑树的性质【不能有2个相连的红色节点】, 需要给父节点进行颜色转换, 因此需要考虑父节点的兄弟(即叔叔节点)节点的颜色

                **情况2.2.1:  叔叔节点是红色**

                > 此时, 父节点和叔叔节点都是红色, 祖父节点是黑色, 违反了红黑树的性质【不能有2个相连的红色节点】, 需要对父节点和叔叔节点进行颜色转换, 同时将祖父节点设置为红色,
                > 因为祖父颜色发生变跟为红色, 所以需要处理以祖父节点为视角的新节点的节点插入

                    **处理**: 将父节点和叔叔节点都设置为黑色, 将祖父节点设置为红色, 然后将祖父节点作为新的插入节点, 继续处理
                    
                    **图例**:
                    
                    ![Uncle is Red](https://media.geeksforgeeks.org/wp-content/uploads/20200506185231/output243.png)

                **情况2.2.2:  叔叔节点是黑色/空(4小类)【需要旋转】**

                > 父节点是红色, 叔叔节点是黑色下, 情况比较复杂, 涉及到树的平衡, 颜色的转换. 有以下4种情况(同平衡二叉树的4种旋转情况)
                > 旋转的目的是为了树的平衡;
                > 旋转完成后, 需要对父节点也进行相同检查

                    **情况2.2.2.1:【父节点红,叔节点黑】  新节点在根节点的左子树节点的左叶子节点, 即Left-Left Case/ LL Case**
                        
                        > 此时新节点在根节点的左子树节点的左叶子节点, 即Left-Left Case/ LL Case, 父节点是红色, 叔叔节点是黑色, 父节点的父节点是黑色, 违反了【不能有2个相连的红色节点(新节点及其父节点)】, 
                        > 因此需要调整节点位置, 将父节点上移, 祖父节点下移, 并将祖父节点设置为红色, 父节点设置为黑色, 即以父节点为根节点的子树进行右旋转
                    
                        
                        **处理**: 将祖父节点设置为红色, 父节点设置为黑色, 以父节点为根节点的子树进行【右旋】  
                        
                        **图例**:
    
                        ![Uncle is Black, LL Case](https://media.geeksforgeeks.org/wp-content/uploads/20200506190350/output244.png)
                        
                    **情况2.2.2.2:【父节点红,叔节点黑】  新节点在根节点的左子树节点的右叶子节点, 即Left-Right Case/ LR Case**
                        
                    > 此时新节点在根节点的左子树节点的右叶子节点, 即Left-Right Case/ LR Case, 父节点是红色, 叔叔节点是黑色, 父节点的父节点是黑色, 违反了【不能有2个相连的红色节点(新节点及其父节点)】,
                    > 因此需要调整节点位置,  先将新节点左旋, 左旋以后就变为【LL Case】, 然后再对当前新节点做为父节点进行【LL Case操作】
                        **处理**: 
                            1. 新节点加入后, 先将新节点【左旋】, 旧的父节点变为新节点的左子节点
                            2. 修改旧父节点的父节点颜色修改为红色, 新节点颜色设置为黑色, 以新节点为根节点的子树进行【右旋】
                        
                        **图例**:
                        
                            ![LR Case](https://media.geeksforgeeks.org/wp-content/uploads/20220319140535/output245copy.png)
                        
                        **测试用例**: `71, 85, 80, 88, 61, 65`

                    
                    **情况2.2.2.3:【父节点红,叔节点黑】  新节点在根节点的右子树节点的右叶子节点, 即Right-Right Case/ RR Case**
                    
                    > 此时新节点在根节点的右子树节点的右叶子节点, 即Right-Right Case/ RR Case, 父节点是红色, 叔叔节点是黑色, 父节点的父节点是黑色, 违反了【不能有2个相连的红色节点(新节点及其父节点)】,
                    > 和【LL Case】情况类似, 只是方向相反, 因此需要调整节点位置, 将父节点上移, 祖父节点下移, 并将祖父节点设置为红色, 父节点设置为黑色, 即以父节点为根节点的子树进行左旋转
                    
                        **处理**: 将祖父节点设置为红色, 父节点设置为黑色, 以父节点为根节点的子树进行【左旋】
                        
                        **图例**:  
                            ![RR Case](https://media.geeksforgeeks.org/wp-content/uploads/20200506190822/output246.png)
                    
                        **测试用例**: `71, 85, 80, 88, 95`
                        
                    
                    **情况2.2.2.4:【父节点红,叔节点黑】  新节点在根节点的右子树节点的左叶子节点, 即Right-Left Case/ RL Case**
                    
                    > 此时新节点在根节点的右子树节点的左叶子节点, 即Right-Left Case/ RL Case, 父节点是红色, 叔叔节点是黑色, 父节点的父节点是黑色, 违反了【不能有2个相连的红色节点(新节点及其父节点)】,
                    > 因此需要调整节点位置, 先将新节点右旋, 右旋以后就变为【RR Case】, 然后再对当前新节点做为父节点进行【RR Case操作】
                    
                        **处理**: 
                            1. 新节点加入后, 先将新节点【右旋】, 旧的父节点变为新节点的右子节点
                            2. 修改旧父节点的父节点颜色修改为红色, 新节点颜色设置为黑色, 以新节点为根节点的子树进行【RR Case操作】
                        
                        **图例**:
                        
                            ![RL Case](https://media.geeksforgeeks.org/wp-content/uploads/20220319140600/output247copy.png)
                    
                        **测试用例**: `71, 85, 80, 88, 95, 92, 100, 120, 110`
        **插入节点总结：**
        1. 【空树插入新节点: 只着色】新节点颜色设置为黑色, 并设置为Root
        2. 【父节点是黑色: 直接插入新节点】, 直接插入新节点, 其他不变
        3. 【父节点是红色, 叔叔节点都是红色:  着色+重复检查祖父节点】, 父节点和叔叔节点都设置为黑色, 祖父节点设置为红色, 重复检查祖父节点
        4. 【父节点是红色, 叔叔节点是黑色: 4种情况-旋转+着色】, 根据新节点的位置进行不同的旋转, 并设置颜色
            LL: 新节点在【左子树的左节点】, 父节点变更为【黑色】,祖父节点变为【红色】, 以【祖父节点】为根节点的子树进行【右旋】
            LR: 新节点在【左子树的右节点】, 新节点的父节点左旋后变为【LL】情况, 修改旧的父节点为【红色】, 新节点为【黑色】, 以新节点为根节点的子树进行【LL Case操作】
            RR: 新节点在【右子树的右节点】, 父节点变更为【黑色】,祖父节点变为【红色】, 以【祖父节点】为根节点的子树进行【左旋】
            RL: 新节点在【右子树的左节点】, 新节点的父节点右旋后变为【RR】情况, 修改旧的父节点为【红色】, 新节点为【黑色】, 以新节点为根节点的子树进行【RR Case操作】
                    
        旋转后着色的情况:
        1. LL Case 和 RR Case: 旋转后交换祖父级和父级的颜色
        2. LR Case 和 RL Case: 旋转后交换祖父级和插入节点的颜色
        
        Args:
            value: 节点的键值
        """
        # 情况1: 插入节点为根节点
        if self.root is None:
            self.root = Node(value)
            self.root.red = False  # 根节点设置为黑色
            return
        # 如果根节点不为空, 则调用插入辅助函数

        self.root = self.insert_helper(self.root, value)

    def insert_helper(self, root, value):
        """
        插入节点的辅助函数
        """
        rr_flag = False  # RED-RED冲突【双红节点冲突】
        if not root:
            # 节点最开始插入的位置
            new_node = Node(value)
            return new_node
        elif value < root.value:
            # 左侧插入
            root.left = self.insert_helper(root.left, value)
            root.left.parent = root
            if root != self.root:
                # 判断是否存在 双红节点
                if root.left.red and root.red:
                    rr_flag = True
        elif value > root.value:
            # 右侧插入
            root.right = self.insert_helper(root.right, value)
            root.right.parent = root
            if root != self.root:
                # 判断是否存在 双红节点
                if root.right.red and root.red:
                    rr_flag = True
        else:
            # 节点已存在
            print(f"Node with value {value} already exists. skipping insertion.")
            return root

        # 旋转处理, 实际是处理下一层新增节点导致的不平衡
        if self.ll:
            # LL Case, 右旋, 基于root节点右旋, root为新增节点的祖父节点
            root = self.right_rotate(root)
            # 新的父节点(原父节点的左节点)
            root.red = False  # 父节点着色为黑色
            root.right.red = True  # 原祖父节点变为红色
            self.ll = False
        elif self.rr:
            # RR Case, 左旋, root为新增节点的祖父节点
            root = self.left_rotate(root)
            root.red = False
            root.left.red = True
            self.rr = False
        elif self.lr:
            # LR Case, 先左旋, 然后执行右旋, root为新增节点的祖父节点
            # 先对父节点进行左旋
            root.left = self.left_rotate(root.left)
            # 然后对当前节点进行右旋
            root = self.right_rotate(root)
            # 交换颜色
            root.red = False
            root.right.red = True
            self.lr = False

        elif self.rl:
            # RL Case, 先右旋, 然后执行左旋, root为新增节点的祖父节点
            # 先对父节点进行右旋
            root.right = self.right_rotate(root.right)
            # 然后对当前节点进行左旋
            root = self.left_rotate(root)
            # 交换颜色
            root.red = False
            root.left.red = True
            self.rl = False

        # 双红处理
        if rr_flag:
            # 存在双红, 情况3: 父节点是红色, 判断叔节点情况, 以下的【父节点】指 当前root
            # 旋转不在这一层操作, 需要递归到上一层完成
            # 1. 判断节点在左右子树的情况
            if root.parent.right == root:
                # 节点在右子树
                # 判断节点情况(即, 判断叔节点颜色, 来确定4中情况及其旋转方式)
                if root.parent.left is None or not root.parent.left.red:
                    # 叔节点是黑色(2种情况， RR Case 和 RL Case)
                    # 判断节点在右子树的左子树还是右子树, 此时: root节点的已存在的节点一定是黑色, 新节点是红色
                    if root.left is not None and root.left.red:
                        # 节点在右子树的左子树, 即 RL Case
                        self.rl = True
                    elif root.right is not None and root.right.red:
                        # 叔节点是黑色(2种情况， RR Case 和 RL Case)
                        # 节点在右子树的右子树, 即 RR Case
                        self.rr = True
                else:
                    # 叔节点是红色, 直接着色, 父节点、叔节点着色为黑色, 祖父节点着色为红色(不能是根节点)
                    root.red = False  # 父节点着色为黑色
                    root.parent.left.red = False  # 叔节点着色为黑色
                    if root.parent != self.root:
                        root.parent.red = True  # 祖父节点着色为红色
            else:
                # 节点在左子树
                if root.parent.right is None or not root.parent.right.red:
                    # 叔节点不存在或者叔节点为黑色(2种情况， LR Case 和 LL Case)
                    if root.left is not None and root.left.red:
                        # 节点在左子树的左子树, 即 LL Case
                        self.ll = True
                    elif root.right is not None and root.right.red:
                        # 节点在左子树的右子树, 即 LR Case
                        self.lr = True
                else:
                    # 叔节点存在且为红色, 直接着色, 父节点,叔节点着色为黑色, 祖父节点着色为红色(不能是根节点)
                    root.red = False  # 父节点着色为黑色
                    root.parent.right.red = False  # 叔节点着色为黑色
                    if root.parent != self.root:
                        root.parent.red = True  # 祖父节点着色为红色
        return root

    def left_rotate(self, node):
        """左旋转
        ![Left Rotate](https://media.geeksforgeeks.org/wp-content/uploads/20200506192055/output250.png)


        1. node 节点下移, node.right节点上移
        2. node.right节点变为node.left节点的左子节点
        3. node的parent节点变为node的右子节点
        4. node节点的右子节点的左子节点partnt变为node
        
        旋转前
        ```
      A
       \
        B
       / \
      C   D

        ```
        
        旋转后
        
        ``` 
        B
       / \
      A   D
       \
        C
        ```

        Args:
            x: 需要左旋转的节点【应该有子节点】
        Returns:
            新的子树根节点
        """

        if node is None or node.right is None:
            return node  # 如果无右子节点则无旋转空间

        # 设定各临时变量
        nr = node.right  # B
        nrl = nr.left  # C
        np = node.parent  # A的父节点(可能为None)

        # 处理当前节点(A)的右子节点(C)及其父关系
        node.right = nrl  # A.right = C
        if nrl is not None:
            nrl.parent = node  # C.parent = A

        # 处理当前节点右子节点(B)及左右子关系
        nr.left = node  # B.left = A
        nr.parent = np  # B.parent 设为原A的父节点

        if np is not None:
            if np.left == node:
                np.left = nr  # 更新原父节点的左子引用
            else:
                np.right = nr  # 更新原父节点的右子引用
        # 注意：不在这里直接修改self.root，让调用者处理

        # 更新当前节点(A)的父节点关系
        node.parent = nr  # A.parent = B

        return nr  # 返回新的子树根

    def right_rotate(self, node):
        """右旋转
        同左旋转, 只是方向相反
        
        1. node节点下移, node.left左子节点上移
        
        
          旋转前
        ```
         A
        /
        B
       / \
      C   D

        ```
        
        旋转后
        
        ``` 
        B
       / \
      C   A
         /
        D
        ```

        Args:
            node (Node): 旋转的节点
        Returns:
            Node: 新的子树根节点
        """
        if node is None or node.left is None:
            return node  # 如果无左子节点则无旋转空间
        # 获取临时变量
        nl = node.left  # B
        nlr = nl.right  # D
        np = node.parent  # A的父节点

        # 处理当前节点(A)的左子节点(D)及其关系
        node.left = nlr
        if nlr is not None:
            nlr.parent = node  # D.parent = A

        # 处理当前节点左子节点(B)及左右关系
        nl.right = node  # B.right = A
        nl.parent = np  # B.parent = A的父节点

        if np is not None:
            if np.left == node:
                np.left = nl  # 更新原父节点的左子引用
            else:
                np.right = nl  # 更新原父节点的右子引用
        else:
            self.root = nl  # 如果A是根节点, 更新根节点为B

        # 更新当前节点(A)的父节点关系
        node.parent = nl  # A.parent = B

        return nl  # 返回新子树根

    def delete(self, value):
        """删除节点


        Args:
            value: 节点的键值
        """
        pass

    def search(self, value):
        """查找节点
        Args:
            value: 节点的键值
        """
        current = self.root
        while current is not None:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:  # value > current.value
                current = current.right
        return None

    def search_helper(self, root, value):
        """
        查找节点的辅助函数(search函数的递归版)
        Args:
            root: 当前节点
            value: 要查找的值
        """
        if root is None:
            return None
        if root.value == value:
            return root
        if value < root.value:
            return self.search_helper(root.left, value)
        return self.search_helper(root.right, value)

    def tree_height(self, node):
        """获取树的高度"""
        if node is None:
            return 0
        return max(self.tree_height(node.left), self.tree_height(node.right)) + 1

    def print(self):
        """打印红黑树"""
        # 打印中序遍历结果
        print("树高度:", self.tree_height(self.root))
        print("中序遍历:", end=" ")
        self._print_midorder(self.root)
        print()
        # 打印树结构
        self.print_tree(self.root)
        print()

    def _print_preorder(self, node):
        """
        打印节点: 前序遍历
        """
        if node is None:
            return
        print(f"{node.value}({'R' if node.red else 'B'})", end=" ")
        self._print_preorder(node.left)
        self._print_preorder(node.right)

    def _print_midorder(self, node):
        """
        打印节点: 中序遍历
        """
        if node is None:
            return
        self._print_midorder(node.left)
        print(f"{node.value}({'R' if node.red else 'B'})", end=" ")
        self._print_midorder(node.right)

    def _print_level_order(self, node):
        """打印节点: 层序遍历"""
        if node is None:
            return
        print(node.value)
        print(node.left)
        print(node.right)

    def print_tree(self, node):
        """打印树结构"""
        if node is None:
            print("空树")
            return

        def print_tree_recursive(node, prefix="", is_left=True):
            """递归打印树结构"""
            if node is None:
                return

            # 打印当前节点
            color = "R" if node.red else "B"
            print(f"{prefix}{'└── ' if is_left else '┌── '}{node.value}({color})")

            # 计算新的前缀
            new_prefix = prefix + ("    " if is_left else "│   ")

            # 递归打印右子树（先打印右子树，这样在控制台中显示更直观）
            if node.right is not None:
                print_tree_recursive(node.right, new_prefix, False)

            # 递归打印左子树
            if node.left is not None:
                print_tree_recursive(node.left, new_prefix, True)

        print("红黑树结构:")
        print_tree_recursive(node)


def main():
    """主函数"""
    rb_tree = RedBlackTree()
    rb_tree.insert(1)
    rb_tree.insert(2)
    rb_tree.insert(3)
    rb_tree.insert(4)
    rb_tree.insert(5)
    rb_tree.insert(6)
    rb_tree.insert(7)
    rb_tree.insert(8)
    rb_tree.print()
    print(rb_tree.search(8))


if __name__ == "__main__":
    main()

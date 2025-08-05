# -*- coding: utf-8 -*-


class Node:
    """A node in a red-black tree."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.red = True

    def uncle(self):
        """获取叔节点"""
        if self.parent is None or self.parent.parent is None:
            return None
        if self.parent.parent.left == self.parent:
            return self.parent.parent.right
        else:
            return self.parent.parent.left

    def is_on_left(self):
        """判断节点是否在左子树"""
        return self.parent.left == self

    def sibling(self):
        """获取兄弟节点"""
        if self.parent is None:
            return None
        if self.is_on_left():
            return self.parent.right
        else:
            return self.parent.left

    def move_down(self, new_parent):
        """
        移动节点到新的父节点

        作用是将当前节点下移，让 new_parent 节点占据原节点的位置，同时更新父子指针。

        Args:
            new_parent: 新的父节点
        """
        # 1. 更新父节点左右子节点
        if self.parent is not None:
            if self.is_on_left():
                self.parent.left = new_parent
            else:
                self.parent.right = new_parent
        # 2. 更新新父节点的父节点
        new_parent.parent = self.parent
        self.parent = new_parent

    def has_red_child(self):
        """判断节点是否有红色子节点"""
        return (self.left is not None and self.left.red) or (
            self.right is not None and self.right.red
        )


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
            LR: 新节点在【左子树的右节点】, 新节点的父节点左旋(不修改节点颜色)后变为【LL】情况,  以新节点的【父节点】为根节点的子树进行【LL Case操作】, 最终新节点颜色为黑色,祖父节点为红色
            RR: 新节点在【右子树的右节点】, 父节点变更为【黑色】,祖父节点变为【红色】, 以【祖父节点】为根节点的子树进行【左旋】
            RL: 新节点在【右子树的左节点】, 新节点的父节点右旋(不修改节点颜色)后变为【RR】情况, 以新节点的【父节点】为根节点的子树进行【RR Case操作】
                    
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

    def successor(self, node):
        """获取后继节点"""
        if node is None:
            return None
        temp = node
        while temp.left is not None:
            temp = temp.left
        return temp

    def bst_replace_node(self, node):
        """
        获取二叉树替换节点(即当前节点的后继叶子节点)
        """
        if node is None or (node.left is None and node.right is None):
            return None
        if node.left is not None and node.right is not None:
            return self.successor(node.right)
        if node.left is not None:
            return node.left
        else:
            return node.right

    def delete_by_value(self, value):
        """删除节点"""
        node = self.search(value)
        if node is None:
            return
        self.delete(node)

    def swap_value(self, v, u):
        """值替换"""
        temp = v.value
        v.value = u.value
        u.value = temp

    def swap_color(self, v, u):
        """颜色替换"""
        temp_red = v.red
        v.red = u.red
        u.red = temp_red

    def delete(self, v):
        """删除节点

        Deletion in Red-Black Tree: https://www.geeksforgeeks.org/dsa/deletion-in-red-black-tree/

        v: 需要删除的节点
        u: 替代节点(后继节点)

        以下是删除红黑树中的节点所涉及的步骤：
        1. If the node to be deleted has no children, simply remove it and update the parent node.
        如果要删除的节点没有子节点，只需将其删除并更新父节点即可。
        2. If the node to be deleted has only one child, replace the node with its child.
        如果要删除的节点只有一个子节点，请将该节点替换为其子节点。
        3. If the node to be deleted has two children, then replace the node with its in-order successor, which is the leftmost node in the right subtree. Then delete the in-order successor node as if it has at most one child.
        如果要删除的节点有两个子节点，则将该节点替换为其按顺序排列的后继节点，即右子树中最左边的节点。然后删除按顺序的后续节点，就好像它最多有一个子节点一样。
        4. After the node is deleted, the red-black properties might be violated. To restore these properties, some color changes and rotations are performed on the nodes in the tree. The changes are similar to those performed during insertion, but with different conditions.
        删除节点后，可能会违反红黑属性。为了恢复这些属性，对树中的节点执行一些颜色更改和旋转。这些变化与插入过程中执行的变化类似，但条件不同。
        5. The deletion operation in a red-black tree takes O(log n) time on average, making it a good choice for searching and deleting elements in large data sets.
        红黑树中的删除作平均需要 O（log n） 时间，使其成为搜索和删除大型数据集中元素的不错选择。


        删除节点处理步骤情况分析:
        > 1. 红黑树插入主要考虑: 双红问题, 在处理双红问题时, 需要考虑叔叔节点(父节点的兄弟节点)的颜色, 来决定旋转方式和着色, 在父节点和叔叔节点都是红色的情况下, 有4种(LL, LR, RR, RL)情况需要处理.
            双红: 新增节点和父节点都是红色节点
        > 2. 红黑树删除主要考虑: 双黑问题, 在处理双黑问题时, 需要考虑被删除节点的兄弟节点的颜色及其子节点颜色, 来决定旋转方式和着色, 在兄弟节点为黑色的情况下, 有4种(LL, LR, RR, RL)情况需要处理.
            双黑: 当一个原本黑色节点被删除时，它的子节点（或 NIL 节点）将获得双重黑色。具体表现为该位置上有两个黑色，因此称为“双黑”, 相当与删除节点和替换节点都是黑节点

        定义: 假设 v 是待删除节点, u 是替代节点(后继节点), parent 是 v 的父节点, sibling 是 v 的兄弟节点

        情况1: v 没有后继节点
            1.1 v是单根节点
            操作: 删除根节点(即树只有1个根节点)

            1.2 v是叶子节点(非None节点),
            - 1. 则检查是否双黑(u,v), 如果是双黑, 则处理双黑
            - 2. 反之, v一定是红色(因为v是叶子节点,那么不是双黑,只有v是红色), 此时如果v有兄弟节点, 则兄弟节点应该设置为红色节点
            操作: 【着色+设置父节点】兄弟节点s设置为红色(【存疑: 待进一步确认是否一定需要操作兄弟节点为红色, 因为兄弟节点大概率本身就是以红色】), 删除v节点, 并更新父节点的左/右子节点为None

        情况2: v 有后继节点u, 则考虑v有几个子节点
            - 1. 如果v只有1个子节点
                - 1.1 判断v是否是root节点 如果是root节点,且存在后继节点u, 则表示根节点只有1个叶子节点
                操作: 将v值替换为u值(颜色不变), 并删除u节点(直接删除)

                - 1.2 反之, 则表示v不是根节点, 表示v有父节点, 则更新父节点左右子节点为u, 更新u节点的父节点, 并删除u, 继续判断uv双黑问题
                    - 1.2.1 如果uv双黑, 则处理u的双黑问题
                    - 1.2.2 反之, 则uv中有一个红色,删除v后,路径中少一个黑色, 那么将u设置为黑色
                    操作: 将u设置为黑色;
                    分析: 如果v为红色, 那么u一定是黑色, u替换v后,路径上少一个黑色节点, 所以将u设置为黑色;
                        如果u为红色, 那么v一定是黑色, 删除v后, 路径上少一个黑色节点, 所以将u设置为黑色;
                        因此: 将u设置为黑色

            - 2. 如果v有2个子节点
            操作: 将v值替换为u值(颜色不变), 并删除u即可(删除u需要走删除节点逻辑)

        双黑问题处理流程:
        1. 判断是否根节点: 根节点不需要处理,直接退出
        2. 检查有没有兄弟节点: 如果没有兄弟节点, 则向上抛出, 处理父节点双黑问题
        3. 如果有兄弟节点, 则判断兄弟节点颜色:
            - 3.1 兄弟节点是红色, 则需要旋转, 旋转后保持原状态的颜色,即新的父节点是原颜色, 新的兄弟节点是原颜色, 将情况转换为兄弟节点是黑色的情况
            操作:
                1. 将兄弟节点的颜色设置为父节点颜色(即黑色,父节点是黑色); 将父节点设置为红色; 相当于删除了一个黑色, 提了一个黑节点(s)上来
                2. 【旋转】： 如果s在左节点，则【以父节点右旋】; 如果s在右节点，则【以父节点左旋】; 旋转后, 原s变为父节点, 原s的右节点变为s,原父节点变为v的位置, 原s的左节点;
                处理完成后，变为了删除节点下移一层, 且新的兄弟节点为黑色场景
                3. 继续处理删除节点的双黑情况
            - 3.2 兄弟节点是黑色
                - 3.2.1 兄弟节点有红色子节点(一个红或者2个都是红色的), 有4种情况(LL, LR, RR, RL)
                    - 情况1: 兄弟节点红色子节点r在左侧
                        - 1.1 兄弟节点在左侧, 即 LL情况(Left Left Case)
                        操作: 【以父节点右旋+交换颜色】, s节点的颜色替换为父节点颜色, r节点颜色替换为s节点颜色, 父节点颜色不变
                        - 1.2 兄弟节点在右侧, 即 RL情况(Right Left Case)
                        操作: 1. 先【以s节点右旋+交换颜色】, 将r节点上移到s节点, 替换为父节点颜色(因为r最终会替换父节点), s下一到r的右节点(颜色不变)
                            2. 再【以父节点左旋】, 旋转后 r节点为原父节点, s节点右子节点为原s节点

                    - 情况2: 兄弟节点红色子节点r在右侧
                        - 2.1 兄弟节点在左侧, 即 LR情况(Left Right Case)
                        操作: 1. 先【以s节点左旋+交换颜色】, 将r节点上移到s节点, 替换为父节点颜色(因为r最终会替换父节点), s下一到r的左节点(颜色不变)
                            2. 再【以父节点右旋】, 旋转后 r节点为原父节点, s节点右子节点为原s节点
                        - 2.2 兄弟节点在右侧, 即 RR情况(Right Right Case)
                        操作: 【以父节点左旋】, s节点的颜色替换为父节点颜色, r节点颜色替换为s节点颜色, 父节点颜色不变


                - 3.2.2 兄弟节点没有红色子节点(2个都是黑色的)
                    1. 将兄弟节点设置为红色(因为要删除v,v是黑色, 少一层黑色节点)
                    2. 如果父节点是黑色, 则继续处理父节点双黑问题
                    3. 如果父节点是红色, 则将父节点设置为黑色, 处理完成


        Args:
            v: 需要删除的节点
        """
        # 1. 获取替代节点(右子树后继节点)
        u = self.bst_replace_node(v)
        # 2. 判断是否双黑
        uv_duble_black = (not v.red) and (u is None or not u.red)
        # 3. 父节点
        parent = v.parent
        # 4. 后继节点为空, 即无子节点, 删除该节点, 并更新父节点
        if u is None:
            # 4.1 如果是根节点, 则删除根节点
            if v == self.root:
                self.root = None
            else:
                # 4.2 如果是叶子节点,检查是否双黑
                if uv_duble_black:
                    # 4.2.1 处理双黑
                    self.fix_double_black(v)
                else:
                    # 4.2.2 不是双黑,那么v是红色, 则更新v的兄弟节点为红色 (因为少一层黑, 所以需要调整)
                    v_sibling = v.sibling()
                    if v_sibling is not None and not v_sibling.red:
                        v_sibling.red = True

                # 并更新父节点
                if v.is_on_left():
                    parent.left = None
                else:
                    parent.right = None
            # 删除节点
            del v
            return

        # 5. 后继节点不为空, 即有子节点, 且只有1个子节点
        if v.left is None or v.right is None:
            # 5.1 v是root节点, 则v值替换为u值, 删除u和左右节点
            if v == self.root:
                v.left = v.right = None
                v.value = u.value
                del u
            else:
                # 5.2 v不是root节点, 即v有父节点
                # 5.2.1 更新父节点左右子节点, 删除节点
                if v.is_on_left():
                    parent.left = u
                else:
                    parent.right = u
                u.parent = parent
                del v
                # 5.2.2 处理双黑
                if uv_duble_black:
                    self.fix_double_black(u)
                else:
                    # 5.2.3 不是双黑, 则v/u是红色,
                    # 如果 u 或 v 中有一个是红色，那么可以直接将 u 设置为黑色。这么做可以避免路径中出现双黑色条件，因为：
                    # 如果 v 是红色，则 u 替代 v 后，将 u 设置为黑色能立即消除路径中的红色节点，不会违反水平衡性。
                    # 如果 u 是红色，则直接设置为黑色，并且在原本的路径中相当于未增加或减少黑色节点的数量。
                    u.red = False
        else:
            # 6. 后继节点不为空, 即有子节点, 且有2个子节点, 则将v值替换为u值,并删除u即可(删除u需要走删除节点逻辑)
            self.swap_value(v, u)
            self.delete(u)

    def fix_double_black(self, node):
        """
        处理双黑节点
        Args:
            node: 需要处理的节点
        """
        if node == self.root:
            return
        # 兄弟节点
        sibling = node.sibling()
        parent = node.parent
        # 1. 如果没有兄弟节点, 则处理父节点双黑(推到上一层处理)
        if sibling is None:
            self.fix_double_black(parent)
        else:
            # 2. 如果有兄弟节点,并且节点是红色的, 旋转并着色,将情况转换为s为黑节点(3.)的情况
            if sibling.red:
                # 如果同级是红色的，则执行旋转以向上移动旧的同级，重新着色旧的同级和父级。新的同级始终是黑色的（见下图: https://media.geeksforgeeks.org/wp-content/cdn-uploads/rbdelete161-1024x704.png）。
                # 这主要将树转换为黑色兄弟情况（通过旋转）并导致 （a） 或 （b）。这种情况可以分为两个子案例。
                #  2.1 Left Case 左子项情况（s 是其父项的左子项）。这是右右情况的镜像, 我们右旋转父 p, s节点设置为黑色, p节点设置为红色
                sibling.red = False
                parent.red = True
                if sibling.is_on_left():
                    self.right_rotate(parent)
                else:
                    # 2.2 Right Case 右子项情况（s 是其父的正确子项）。我们左旋转父 p。
                    self.left_rotate(parent)
                self.fix_double_black(node)

            else:
                # 3. 如果有兄弟节点,并且节点是黑色的
                # 3.1 如果兄弟姐妹 s 是黑色的，并且兄弟姐妹的至少一个孩子是红色的，则执行轮换。让 s 的红色子是 r。这种情况可以根据 s 和 r 的位置分为四个子情况。
                if sibling.has_red_child():
                    # 3.1.1 s左节点是红色
                    if sibling.left is not None and sibling.left.red:
                        # 3.1.1 Left Left Case, 左左情况, s为父节点的左节点, r为s的左节点; (s 是其父项的左子项，r 是 s 的左项子项，或者 s 的两个子项都是红色的)
                        # 旋转+着色: 以父节点p为支点, s节点右子节点颜色替换为s节点颜色, s节点的颜色替换为父节点颜色, 然后以p节点为支点, 【右旋转p】
                        if sibling.is_on_left():
                            # 1. s左子节点颜色替换为原s节点颜色
                            sibling.left.red = sibling.red
                            # 2. s节点颜色替换为父节点颜色
                            sibling.red = parent.red
                            # 3. 以父节点p为支点, 【右旋转p】, 旋转后 s节点为原父节点, s节点左子节点为原s节点
                            self.right_rotate(parent)
                        else:
                            # 3.1.2 Right Left Case, 右左情况, s为父节点的左节点, r为s的右节点
                            # 旋转+着色: 【s右旋+p左旋】
                            # 1. 先以s节点为支点, 【右旋转s】, 将r节点上移到s节点, 替换为s父节点的颜色(因为r最终会替换父节点), s下一到r的右节点(颜色不变)
                            sibling.left.red = parent.red
                            self.right_rotate(sibling)
                            # 2. 再以父节点p为支点, 【左旋转p】, 旋转后 r节点为原父节点, s节点右子节点为原s节点
                            self.left_rotate(parent)
                    else:
                        # 3.2.1 s右节点是红色
                        # 3.2.1 Left Right Case, 左右情况, s为父节点的右节点, r为s的左节点
                        # 旋转+着色: 【s左旋+p右旋】, s颜色不变, r颜色替换为p颜色, 最终r在p的位置, s还在原位置, p成为r的右节点,颜色不变
                        if sibling.is_on_left():
                            sibling.right.red = parent.red
                            self.left_rotate(sibling)
                            self.right_rotate(parent)

                        else:
                            # 3.2.2 Right Right Case, 右右情况, s为父节点的右节点, r为s的右节点 （s 是其父项的右子项，r 是 s 的右项子项，或 s 的两个子项均为红色）
                            # 旋转+着色: 以父节点p为支点, 【左旋转p】, 旋转后 s节点为原父节点
                            # 1. s右子节点颜色替换为原s节点颜色
                            sibling.right.red = sibling.red
                            # 2. s节点颜色替换为父节点颜色
                            sibling.red = parent.red
                            # 3. 以父节点p为支点, 【左旋转p】, 旋转后 s节点为原父节点
                            self.left_rotate(parent)
                else:
                    # 4. 子节点都是黑色的; 如果同级是黑色的，并且它的两个子级都是黑色的，则执行重新着色，如果父级是黑色，则为父级重复。
                    sibling.red = True
                    if not parent.red:
                        self.fix_double_black(parent)
                    else:
                        parent.red = False

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
        self._print_inorder(self.root)
        print()
        # 打印树结构
        self.print_tree(self.root)
        print()

    ##########
    # 树的遍历 START
    ##########

    def _print_preorder(self, node):
        """
        打印节点: 前序遍历
        """
        if node is None:
            return
        print(f"{node.value}({'R' if node.red else 'B'})", end=" ")
        self._print_preorder(node.left)
        self._print_preorder(node.right)

    def _print_inorder(self, node):
        """
        打印节点: 中序遍历
        """
        if node is None:
            return
        self._print_inorder(node.left)
        print(f"{node.value}({'R' if node.red else 'B'})", end=" ")
        self._print_inorder(node.right)

    def _print_postorder(self, node):
        """
        打印节点: 后序遍历
        """
        if node is None:
            return
        self._print_postorder(node.left)
        self._print_postorder(node.right)
        print(f"{node.value}({'R' if node.red else 'B'})", end=" ")

    def _print_level_order(self, node):
        """打印节点: 层序遍历"""
        if node is None:
            return
        # TODO
        print(node.value)
        print(node.left)
        print(node.right)

    ##########
    # 树的遍历 END
    ##########
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
    print("删除节点5")
    rb_tree.delete_by_value(5)
    rb_tree.print()
    print(rb_tree.search(8))


if __name__ == "__main__":
    main()

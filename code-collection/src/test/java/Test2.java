import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * @author kango2gler@gmail.com
 * @date 2024/6/15
 * @since
 */
public class Test2 {
    public static void main(String[] args) {
//        int[] nums =new int[]{-4,-1,-1,0,1,2};
//        System.out.println(threeSum(nums));
//        testReverseList();
//        testIsPalindrome();
//        testMergeTwoLists();
//        testMaxProfit();
//        testClimbStairs();
//        testGenerate();
//        testMaxSubArray();
//        testSetZeroes();
//        testSpiralOrder();
//        testRotate();
        testSearchMatrix();
    }

    public static List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        int len = nums.length;
        List<List<Integer>> ret = new ArrayList<>();
        // 3个for循环解决
        // -4,-1,-1,0,1,2
        Integer preIVal = null;
        for (int i = 0; i < len; ++i) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int k = len - 1;
            int targetValue = -nums[i];
            for (int j = i + 1; j < len; ++j) {
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;
                // 保证j在k左侧,且相加>目标值,左移k
                if (j < k && nums[j] + nums[k] > targetValue) {
                    --k;
                }
                // j和k重合时退出
                if (j == k) break;
                if (nums[j] + nums[k] == targetValue) {
                    ret.add(Arrays.asList(nums[i], nums[j], nums[k]));
                }
            }
        }
        return ret;
    }

    public static class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }

        @Override
        public String toString() {
            return val + "";
        }
    }

    public static ListNode reverseList(ListNode head) {
        ListNode ret = new ListNode();
        reverse(head, ret);
        return ret.next;
    }

    public static ListNode reverse(ListNode head, ListNode retHead) {
        if (head == null) {
            return retHead;
        }
        ListNode next = reverse(head.next, retHead);
        next.next = new ListNode(head.val);
        return next.next;
    }

    public static void testReverseList() {
        ListNode node = new ListNode(1);
        ListNode s = node;
        for (int i = 1; i < 5; i++) {
            node.next = new ListNode(i + 1);
            node = node.next;
        }
        ListNode ret = reverseList(s);
        System.out.println(ret);
    }

    public static void testIsPalindrome() {
        ListNode node = new ListNode(1, new ListNode(2, new ListNode(2, new ListNode(1))));
//        ListNode node = new ListNode(1,new ListNode(2));
//        ListNode node = new ListNode(1);
        System.out.println(isPalindrome2(node));
    }

    public static boolean isPalindrome(ListNode head) {
        int nodeLen = 0;
        ListNode temp = head;
        while (temp != null) {
            nodeLen++;
            temp = temp.next;
        }
        if (nodeLen % 2 > 0) {
            return false;
        }
        // 找到中间值, 中间值链表反转, 与中间值后的依次比较
        int middle = nodeLen / 2;
        int currIdx = 0;
        ListNode pre = null;
        ListNode curr = head;
        while (curr != null) {
            ListNode next = curr.next;
            if (currIdx >= middle) {
                if (pre.val != curr.val) {
                    return false;
                }
                pre = pre.next;
            } else {
                curr.next = pre;
                pre = curr;
            }
            curr = next;
            currIdx++;
        }
        return currIdx == nodeLen;
    }

    public static boolean isPalindrome2(ListNode head) {
        if (head == null || head.next == null) return true;
        // 快慢指针找中间节点, 反转中间节点后的链表和中间节点前的链表比较
        ListNode fast = head;
        // 中间节点
        ListNode slow = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        // 反转后续节点
        ListNode backHalfNode = null;
        ListNode curr = slow;
        while (curr != null) {
            ListNode next = curr.next;
            curr.next = backHalfNode;
            backHalfNode = curr;
            curr = next;
        }
        ListNode checkNode = head;
        ListNode checkBackNode = backHalfNode;
        // 比较前段节点和后段
        while (checkNode != null && checkBackNode != null) {
            if (checkNode.val != checkBackNode.val) {
                return false;
            }
            checkNode = checkNode.next;
            checkBackNode = checkBackNode.next;
        }
        return true;
    }

    public static void testMergeTwoLists() {
        ListNode node1 = new ListNode(1, new ListNode(2, new ListNode(4)));
        ListNode node2 = new ListNode(1, new ListNode(3, new ListNode(4)));
        System.out.println(mergeTwoLists(node1, node2));
    }

    public static ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null) return list2;
        if (list2 == null) return list1;
        ListNode n1 = list1;
        ListNode n2 = list2;
        ListNode ret = new ListNode();
        ListNode curr = ret;
        while (n1 != null || n2 != null) {
            if (((n1 != null && n2 != null) && n1.val >= n2.val) || n1 == null) {
                curr.next = n2;
                n2 = n2.next;
            } else {
                curr.next = n1;
                n1 = n1.next;
            }
            curr = curr.next;
            curr.next = null;
        }
        return ret.next;
    }


    public static void testMaxProfit() {
        int[] prices = {1, 2};
        System.out.println(maxProfit(prices));
    }

    public static int maxProfit(int[] prices) {
        if (prices == null || prices.length == 0) return 0;
        // dp动态规划问题
        // dp[0] = 0;
        // dp[1] = max(dp[0],prices[1] - prices[0]);
        // dp[2] = max(dp[1], prices[2]-prices[1], prices[2]-prices[0]);
        // dp[3] = max(dp[2], prices[3]-prices[2], prices[3]-prices[1],prices[3]-prices[0]);
        // dp[4] = max(dp[3], prices[4]-prices[3], prices[4]-prices[2],prices[4]-prices[1],prices[4]-prices[0]);
        // dp[n] = max(dp[n-1], prices[n] - prices[n-1],....,prices[n]-prices[0])

        int len = prices.length;
        int[] dp = new int[len];
        int i = 0;
        while (i < len) {
            if (i == 0) {
                dp[i] = 0;
            } else {
                int val = dp[i - 1];
                int j = i;
                while (j >= 0) {
                    val = Math.max(val, prices[i] - prices[j]);
                    j--;
                }
                dp[i] = val;
            }
            i++;
        }
        return dp[len - 1];
    }

    public static void testClimbStairs() {
        System.out.println(climbStairs(4));
    }

    public static int climbStairs(int n) {
        if (n <= 2) return n;
        // 动态规划解法: 1维数组
        // dp[0]: 0
        // dp[1]: 1
        // dp[2]: dp[1] + 1 2
        // dp[3]: dp[2] + dp[1] 3
        // dp[4]: dp[3] + dp[2]  5
        int[] dp = new int[n + 1];
        dp[0] = 0;
        dp[1] = 1;
        dp[2] = 2;
        int i = 3;
        while (i <= n) {
            dp[i] = dp[i - 1] + dp[i - 2];
            i++;
        }
        return dp[n];
    }


    public static void testGenerate() {
        System.out.println(generate(5));
    }

    public static List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ret = new ArrayList<>();
        for (int i = 0; i < numRows; i++) {
            List<Integer> level = new ArrayList<>();
            level.add(1);
            for (int j = 0; j <= i - 1; j++) {
                List<Integer> preLevel = ret.get(i - 1);
                level.add(preLevel.get(j) +
                        (j + 1 < preLevel.size() ? preLevel.get(j + 1) : 0));
            }
            ret.add(level);
        }
        return ret;
    }

    public static void testMaxSubArray() {
        System.out.println(maxSubArray(new int[]{-2, 1, -3, 4, -1, 2, 1, -5, 4}));
    }

    public static int maxSubArray(int[] nums) {
        if (nums.length == 0) return 0;
        // 最大和的连续子数组
        // 1. 暴力法(超时)
        // 2. 动态规划(当前解法)
        // a. 定义状态转移方程方程
        // dp[i] 为第i个数结尾的最大和
        // dp[i] = max(dp[i-1]+nums[i], nums[i])
        // b. 最大值
        // maxSum = max(dp[i], maxSum)
        // c. 初始化
        // dp[0] = nums[0]
        int maxSum = nums[0];
        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            dp[i] = Math.max(dp[i - 1] + nums[i], nums[i]);
            maxSum = Math.max(dp[i], maxSum);
        }
        return maxSum;
    }

    public static void testSetZeroes() {
        int[][] matrix = new int[][]{{1, 0, 3}};
        setZeroes(matrix);
        System.out.println(Arrays.toString(matrix));
    }

    public static void setZeroes(int[][] matrix) {
        // O(1)空间复杂度解法: 将第一行,第一列用来记录是否需要置零
        int m = matrix.length;
        int n = matrix[0].length;
        // 行
        boolean firstRowZero = false;
        // 列
        boolean firstLineZero = false;
        for (int i = 0; i < m; i++) {
            if (matrix[i][0] == 0) {
                firstLineZero = true;
                break;
            }
        }
        for (int i = 0; i < n; i++) {
            if (matrix[0][i] == 0) {
                firstRowZero = true;
                break;
            }
        }
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }
        if (firstRowZero) {
            for (int i = 0; i < n; i++) {
                matrix[0][i] = 0;
            }
        }
        if (firstLineZero) {
            for (int i = 0; i < m; i++) {
                matrix[i][0] = 0;
            }
        }
    }


    public static void testSpiralOrder() {
//        int[][] matrix = new int[][]{{1,2,3},{4,5,6},{7,8,9}};
        int[][] matrix = new int[][]{{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
        System.out.println(spiralOrder(matrix));
    }

    public static List<Integer> spiralOrder(int[][] matrix) {
        // 按上 右 下 左的方式遍历二维数组
        int m = matrix.length;
        int n = matrix[0].length;
        List<Integer> ret = new ArrayList<>();
        int left = 0, right = n - 1, top = 0, bottom = m - 1;
        while (left <= right && right >= 0 && top <= bottom && bottom >= 0) {
            // 上
            for (int i = left; i <= right && top <= bottom; i++) ret.add(matrix[top][i]);
            top++;
            // 右
            for (int i = top; i <= bottom && left <= right; i++) ret.add(matrix[i][right]);
            right--;
            // 下
            for (int i = right; i >= left && top <= bottom; i--) ret.add(matrix[bottom][i]);
            bottom--;
            // 左
            for (int i = bottom; i >= top && left <= right; i--) ret.add(matrix[i][left]);
            left++;
        }
        return ret;
    }

    public static void testRotate() {
//        int[][] matrix = new int[][]{{1,2,3},{4,5,6},{7,8,9}};
        int[][] matrix = new int[][]{{5, 1, 9, 11}, {2, 4, 8, 10}, {13, 3, 6, 7}, {15, 14, 12, 16}};
        rotate(matrix);
        System.out.println(matrix);
    }

    public static void rotate(int[][] matrix) {
        // 思路: 一层一层旋转, 临时变量t 保存被旋转替换的值,直到最内层旋转完成
        // 变换规则: n为矩阵长度, i,j为坐标
        int n = matrix.length;
        // 旋转n/2次, 包含n为基数、偶数
        for (int i = 0; i < n / 2; i++) {
            // 从第i层开始
            for (int j = 0; j < (n+1)/2; j++) {
                // 旋转的临时变量, 第四个左下角的值
                int t = matrix[i][j];
                matrix[i][j] = matrix[n - j - 1][i];
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1];
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1];
                matrix[j][n - i - 1] = t;
            }
        }
    }

    public static void testSearchMatrix() {
//        int[][] matrix = new int[][]{{1,2,3},{4,5,6},{7,8,9}};
//        int[][] matrix = new int[][]{{1,4,7,11,15},{2,5,8,12,19},{3,6,9,16,22},{10,13,14,17,24},{18,21,23,26,30}};
//        int target = 5;
//        int[][] matrix = new int[][]{{1,2,3,4,5},{6,7,8,9,10},{11,12,13,14,15},{16,17,18,19,20},{21,22,23,24,25}};
//        int target = 19;
        int[][] matrix = new int[][]{{5},{6}};
        int target = 6;
        System.out.println(searchMatrix2(matrix,target));
    }
    public static boolean searchMatrix(int[][] matrix, int target) {
        // 特点, 横向升序, 纵向升序
        int m = matrix.length;
        int n = matrix[0].length;
        // 1. 二分法先定位行,找到行, 再二分法定位列
        for (int col = 0; col < m; col++) {
            int left = 0, right = n - 1;
            while (left <= right){
                int mid = (left + right) / 2;
                if (matrix[col][mid] < target){
                    left = mid + 1;
                }else if (matrix[col][mid] > target){
                    right = mid - 1;
                }else {
                    return true;
                }
            }
        }
        return false;
    }
    public static boolean searchMatrix2(int[][] matrix, int target) {
        // 特点, 横向升序, 纵向升序
        int m = matrix.length;
        int n = matrix[0].length;
        int eachCnt = m > n ? n : m;
        int eachRight = m > n ? m : n;
        // 1. 二分法循环行扫描
        for (int i = 0; i < eachCnt; i++) {
            int left = 0, right = eachRight - 1;
            while (left <= right) {
                int mid = (left + right) / 2;
                int col = m > n ? i : mid;
                int row = m > n ? mid : i;
                if (matrix[row][col] < target) {
                    left = mid + 1;
                } else if (matrix[row][col] > target) {
                    right = mid - 1;
                } else {
                    return true;
                }
            }
        }
        return false;
    }
}


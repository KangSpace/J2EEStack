package org.kangspace.j2eestack.main.algorithms.topn;

import java.util.*;

/**
 * 使用堆实现Top N
 * @author kango2gler@gmail.com
 * @since 2023/7/18
 */
public class TopNHeap {
    public static List<Integer> topN(int[] nums, int n) {
        PriorityQueue<Integer> heap = new PriorityQueue<>(n, Comparator.naturalOrder());
        for (int num : nums) {
            if (heap.size() < n) { // 堆还没有填满
                heap.offer(num);
            } else if (num > heap.peek()) { // 新元素比堆顶元素大
                heap.poll();
                heap.offer(num);
            }
        }
        List<Integer> result = new ArrayList<>(heap);
        Collections.sort(result, Collections.reverseOrder()); // 逆序排列
        return result;
    }

    public static void main(String[] args) {
        int[] nums = {9, 3, 2, 4, 8, 7, 5, 1, 6};
        int n = 3;
        List<Integer> topN = topN(nums, n);
        System.out.println(topN); // 输出 [9, 8, 7]
    }
}

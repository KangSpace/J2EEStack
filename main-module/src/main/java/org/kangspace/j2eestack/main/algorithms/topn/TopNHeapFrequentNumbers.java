package org.kangspace.j2eestack.main.algorithms.topn;
import java.util.*;

/**
 * 找到1亿个数中，出现频率最高的n个数 <br>
 * 可以使用一个小根堆来维护当前出现频率最高的n个数，遍历所有的数，将它们加入小根堆中，如果小根堆的大小超过了n，就将堆顶元素弹出。最后，剩下的n个数就是出现频率最高的n个数。 <br>
 * 为了统计每个数的出现频率，可以使用一个哈希表来存储每个数出现的次数。遍历所有的数，将它们添加到哈希表中，如果哈希表中已经存在该数，则将它的出现次数加一，否则将它的出现次数设为1 <br>
 */
public class TopNHeapFrequentNumbers {
    public static List<Integer> topNFrequent(int[] nums, int n) {
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        for (int num : nums) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }

        PriorityQueue<Map.Entry<Integer, Integer>> heap = new PriorityQueue<>(
                Comparator.comparingInt(Map.Entry::getValue));

        for (Map.Entry<Integer, Integer> entry : frequencyMap.entrySet()) {
            heap.offer(entry);
            if (heap.size() > n) {
                heap.poll();
            }
        }

        List<Integer> result = new ArrayList<>();
        while (!heap.isEmpty()) {
            result.add(heap.poll().getKey());
        }
        Collections.reverse(result);
        return result;
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4, 5, 1, 2, 3, 4, 1, 2, 3, 1, 2, 1};
        int n = 3;
        List<Integer> topN = topNFrequent(nums, n);
        System.out.println(topN); // 输出 [2, 3, 1]
    }
}
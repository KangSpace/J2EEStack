package org.kangspace.j2eestack.main.algorithms.topn;

import java.util.ArrayList;
import java.util.List;

/**
 * 找到1亿个数中，出现频率最高的n个数 <br>
 * 当提供的数足够多时，使用哈希表来统计每个数的出现频率可能会消耗大量的内存，因此可以考虑使用更为节省空间的数据结构。一种常见的做法是使用桶排序算法。 <br>
 * 具体来说，可以先使用桶排序算法统计每个数出现的次数，并将它们存储在一个桶中。然后，可以从桶中选择出现频率最高的n个数。具体的做法是，从桶中选出出现频率最高的数，将它添加到结果数组中，如果结果数组的大小已经达到了n，就返回结果数组；否则，继续从桶中选出出现频率次高的数，重复这个过程，直到结果数组的大小达到n。 <br>
 */
public class TopNBucketFrequentNumbers {
    public static List<Integer> topNFrequent(int[] nums, int n) {
        int maxNum = Integer.MIN_VALUE;
        int minNum = Integer.MAX_VALUE;
        // 找出最大、最小值
        for (int num : nums) {
            maxNum = Math.max(maxNum, num);
            minNum = Math.min(minNum, num);
        }

        // 找出桶数量, 并计算每个数的数量
        int[] buckets = new int[maxNum - minNum + 1];
        for (int num : nums) {
            buckets[num - minNum]++;
        }

        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int maxIndex = 0;
            for (int j = 1; j < buckets.length; j++) {
                if (buckets[j] > buckets[maxIndex]) {
                    maxIndex = j;
                }
            }
            if (buckets[maxIndex] == 0) {
                break;
            }
            result.add(maxIndex + minNum);
            buckets[maxIndex] = 0;
        }
        return result;
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4, 5, 1, 2, 3, 4, 1, 2, 3, 1, 2, 1};
        int n = 3;
        List<Integer> topN = topNFrequent(nums, n);
        System.out.println(topN); // 输出 [2, 3, 1]
    }
}
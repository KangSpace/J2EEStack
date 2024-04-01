package org.kangspace.j2eestack.main.algorithms.datastructure.sort.test;

import java.util.Arrays;

/**
 * 排序测试集合
 *
 * @author kango2gler@gmail.com
 * @date 2024/3/18
 * @since
 */
public class SortTest {

    /**
     * 快排测试:
     * 1. 快排: 取基准值，将小于基准值的值放到左边,大于基准值的值放到右边
     * 2. 将数组分为2个子数组，再分别进行快排
     */
    public static class QuickSort {

        public static void sort(int[] arr) {
            sort(arr, 0, arr.length - 1);
        }


        /**
         * 快速排序:
         * 1. 获取基准值 索引
         * 2. 将数组拆分为2个子数组，再分别进行快排排序
         * <img src="https://www.runoob.com/wp-content/uploads/2019/03/quickSort.gif"/>
         *
         * @param arr
         * @param left
         * @param right
         */
        public static void sort(int[] arr, int left, int right) {
            if(left < right) {
                int index = partition(arr, left, right);
                sort(arr, left, index - 1);
                sort(arr, index + 1, right);
            }
        }


        /**
         * 获取基准值索引，并将小于基准值的值放到左边，大于基准值的值放到右边
         *
         * @param arr
         * @return
         */
        public static int partition(int[] arr, int left, int right) {
            int partition = arr[left];
            int index = left + 1;
            // 将后续的值和基准值进行比较:
            // 1. 基准值占第一个数组位置
            // 2. 将后续小于基准值的值和基准值后的一个位置替换
            for (int i = index; i <= right; i++) {
                // 小于基准值时, 将该值和基准值交换
                if (arr[i] < partition) {
                    // 当i>基准值index时做替换, 即,如果第2个元素大于基准值时,不做替换
                    if (i > index) {
                        swap(arr, i, index);
                    }
                    index++;
                }
            }
            index = index - 1;
            // 3. 最后替换最后一个小的数和基准值的位置
            swap(arr, left, index);
            return index;
        }
    }

    public static void swap(int[] arr, int i, int index) {
        int temp = arr[i];
        arr[i] = arr[index];
        arr[index] = temp;
    }

    public static void main(String[] args) {
        int[] arr = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21};
        QuickSort.sort(arr);
        System.out.println(Arrays.toString(arr));
    }
}

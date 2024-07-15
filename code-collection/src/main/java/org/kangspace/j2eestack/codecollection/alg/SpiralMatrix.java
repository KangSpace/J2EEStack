package org.kangspace.j2eestack.codecollection.alg;

import java.util.Arrays;

/**
 * 螺旋矩阵
 * //1 2 3 4 5
 * //16 17 18 19 6
 * //15 24 25 20 7
 * //14 23 22 21 8
 * //13 12 11 10 9
 * // 输入一个数字 5 打印 5x5矩阵
 * // 内螺旋矩阵
 *
 * @author kango2gler@gmail.com
 * @date 2024/6/26
 */
public class SpiralMatrix {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(spiralMatrix(5)));
    }

    public static int[][] spiralMatrix(int n) {
        // 使用坐标构建
        // 定义NxN二维数组
        int[][] ret = new int[n][n];
        int val = 1;
        // 定义坐标
        int left = 0, right = n - 1, top = 0, bottom = n - 1;
        while (val <= n * n) {
            // 第一行 从左到右
            for (int i = left; i <= right && val <= n * n; i++) {
                ret[top][i] = val++;
            }
            top++;
            // 最后一列 从上到下
            for (int i = top; i <= bottom && val <= n * n; i++) {
                ret[i][right] = val++;
            }
            right--;
            // 最后一行 从右到左
            for (int i = right; i >= left && val <= n * n; i--) {
                ret[bottom][i] = val++;
            }
            bottom--;
            // 第一列 从下到上
            for (int i = bottom; i >= top && val <= n * n; i--) {
                ret[i][left] = val++;
            }
            left++;
        }
        return ret;
    }
}

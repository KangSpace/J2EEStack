package org.kangspace.j2eestack.codecollection.alg;

/**
 * @author kango2gler@gmail.com
 * @date 2024/6/27
 * @since
 */
public class RevertString {
    public static void main(String[] args) {
        // 字符串反转
        System.out.println(revertStr("abcdefg"));

    }

    public static String revertStr(String str) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < str.length(); i++) {
            sb.insert(0, str.charAt(i));
        }
        return sb.toString();
    }
}

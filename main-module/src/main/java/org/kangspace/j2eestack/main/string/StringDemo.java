package org.kangspace.j2eestack.main.string;

import lombok.extern.slf4j.Slf4j;

/**
 * 字符串相关demo
 *
 * @author kango2gler@gmail.com
 * @since 2022/10/25
 */
@Slf4j
public class StringDemo {

    public static void aAddB() {
        String a = "a";
        String b = "b";
        String ab = "ab";
        String aAndB = "a"+"b";
        String c = a + b;
        String d = "a" + b;
        boolean cEqualAb = c == ab;
        boolean abEqualAAndB = ab == aAndB;
        log.info("a:{}", a.hashCode());
        log.info("b:{}", b.hashCode());
        log.info("ab:{}", ab.hashCode());
        log.info("c:{}", c.hashCode());
        log.info("c == ab:{}", cEqualAb);
        log.info("ab == a+b:{}", abEqualAAndB);
        log.info("d:{}", d);
    }

    public static void main(String[] args) {
        aAddB();
    }
}

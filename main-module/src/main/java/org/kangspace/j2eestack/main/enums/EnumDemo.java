package org.kangspace.j2eestack.main.enums;

/**
 * @author kango2gler@gmail.com
 * @since 2022/10/27
 */
public enum EnumDemo {
    APPLE(0),
    BANANA(1),
    GREEN(3),
    ;
    private int id;
    EnumDemo(int id){
        this.id = id;
    }

    public static void main(String[] args) {
        System.out.println(EnumDemo.valueOf("APPLE"));
        System.out.println(EnumDemo.GREEN.ordinal());
    }
}

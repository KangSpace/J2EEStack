package org.kangspace.j2eestack.main.clazz;

import java.lang.annotation.Documented;

/**
 * 基本数据类型转换
 *
 * @author kango2gler@gmail.com
 * @date 2024/3/1
 */
public class BasicTypeConversion {
    public static void main(String[] args) {
        // byte
//        g((byte) 1);
//        g(Byte.parseByte("1"));
        // char
//        g('1');
        // short
//        g(Integer.valueOf(1).shortValue());
        // int
//        g(1);
        // Integer
//        g(Integer.valueOf(1));
        // float
//        g(1.1f);
        // Float
//        g(new Float(.1f));
        // Double
//        g(1D);
        System.out.println();
        /*
        1. 基本数据类型自动转换优先级:
        a. (byte -> short)、char -> int (byte, char无法自动相互转换, byte 可自动转换为 short)
        b. int之后依次为: long, float, double
        c. 找不到以上基础类型数据时,再找该基本数据类型对应的包装类型
            - 不同的基础类型转换只能转换为基础数据类型，不能转换为包装类型
            - 包装类型在没有对应包装类型的方法时，可以转换为更高级的基础数据类型，如:Integer 转为 long 及以上 ,Float 转为 double 及以上
            - 包装类型不能自动转换
        2. byte, char 可以强制类型互转, 但可能会出现精度丢失(如char是2字节字符时, 转换为byte时, 会丢失)
         */
    }


//    static void g(byte b) {
//        System.out.println("Byte:" + b);
//    }

//    static void g(Byte b) {
//        System.out.println("Byte:" + b);
//    }

//    static void g(char c) {
//        System.out.println("char:" + c);
//    }

//    static void g(Character c) {
//        System.out.println("Integer:" + c);
//    }

//    static void g(short i) {
//        System.out.println("short:" + i);
//    }
//
//    static void g(Short i) {
//        System.out.println("Short:" + i);
//    }

//    static void g(int i) {
//        System.out.println("int:" + i);
//    }
//    static void g(Integer i) {
//        System.out.println("Integer:" + i);
//    }

    static void g(Long l) {
        System.out.println("Long:" + l);
    }

//    static void g(long l) {
//        System.out.println("Long:" + l);
//    }

//    static void g(float f) {
//        System.out.println("float:"+f);
//    }

//    static void g(Float f) {
//        System.out.println("Float:"+f);
//    }

//    static void g(double d) {
//        System.out.println("double:" + d);
//    }

//    static void g(Double s) {
//        System.out.println("Integer:" + s);
//    }
}

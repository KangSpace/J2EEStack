package org.kangspace.j2eestack.main.clazz;

import org.kangspace.j2eestack.main.enums.EnumDemo;

/**
 * Switch Demo
 * @author kango2gler@gmail.com
 * @since 2022/10/27
 */
public class SwitchDemo {
    public static void main(String[] args) {
        int a = 1024;
        switch (a){
            case 1: break;
            case 1024: break;
        }

        String b = "b";
        switch (b) {
            case "": break;
            case "b": break;
        }

        EnumDemo c = EnumDemo.APPLE;
        switch (c) {
            case BANANA: break;
            case GREEN: break;
        }
    }
}

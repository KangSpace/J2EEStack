package org.kangspace.j2eestack.main.clazz;

/**
 * 变长参数Demo
 * @author kango2gler@gmail.com
 * @since 2022/10/27
 */
public class VariableLengthArgumentsDemo {
    public void variableLength(Object... args) {
        Object[] o = args;
        System.out.println(o);
    }
}

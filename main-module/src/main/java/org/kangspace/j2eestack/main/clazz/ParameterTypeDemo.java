package org.kangspace.j2eestack.main.clazz;

/**
 * 泛型参数Demo
 * @author kango2gler@gmail.com
 * @since 2022/10/28
 */
public class ParameterTypeDemo<T extends ParameterTypeDemo> {
    private T t;
    public static void main(String[] args) {
        ParameterTypeDemo<A> parameterTypeDemo = new ParameterTypeDemo<>();
        System.out.println(parameterTypeDemo.t);
    }

    static class A extends ParameterTypeDemo{}
}

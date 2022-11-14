package org.kangspace.j2eestack.main.clazz;

/**
 * Lambda Demo
 *
 * @author kango2gler@gmail.com
 * @since 2022/10/28
 */
public class ClassDemo {

    public static void main(String[] args) {
        class SimpleInnerClass{}
        SimpleInnerClass simpleInnerClass = new SimpleInnerClass();
        System.out.println(simpleInnerClass);
        {
            abstract class CodeBlockInMethodClass{}
            CodeBlockInMethodClass codeBlockInMethodClass = new CodeBlockInMethodClass(){};
            CodeBlockInMethodClass codeBlockInMethodClass2 = new CodeBlockInMethodClass(){};
            System.out.println(codeBlockInMethodClass);
            System.out.println(codeBlockInMethodClass2);
        }
        simpleInnerClass = new SimpleInnerClass(){};
        SimpleInterface simpleInterface = (t)-> System.out.println(t);
        SimpleInterface simpleInterface2 = (t)-> System.out.println(t);
        Simple2Interface simple2Interface = (t)-> System.out.println(t);
        System.out.println("simpleInterface:"+ simpleInterface.getClass());
        System.out.println("simpleInterface2:"+ simpleInterface2.getClass());
        System.out.println("simple2Interface:"+ simple2Interface.getClass());
    }

    @FunctionalInterface
    interface SimpleInterface{
        void run(String msg);
    }
    @FunctionalInterface
    interface Simple2Interface{
        void run(String msg);
    }
    static {
        class TEMP{
            public void main(String[] args) {
                class TEMP_MAIN_METHOD_CLASS{}
            }
            class INNER_TEMP{}
        }
    }
}

package org.kangspace.j2eestack.main.clazz;

/**
 * 父子类测试
 * @author kango2gler@gmail.com
 * @date 2024/4/1
 * @since
 */
public class ParentChildrenClass {
    public static class ParentClass {
        public void run(){
            System.out.println("ParentClass run");
            this.run2();
        }

        public void run2(){
            System.out.println("ParentClass run2");
        }
    }

    public static class ChildrenClass extends ParentClass {
        public void run(){
            System.out.println("ChildrenClass run");
        }

        public void run2(){
            System.out.println("ChildrenClass run2");
        }

        public void callParentRun() {
            System.out.println("ChildrenClass callParentRun");
            super.run();
        }
    }

    public static void main(String[] args) {
        ChildrenClass childrenClass = new ChildrenClass();
        childrenClass.run();
        childrenClass.callParentRun();
    }
}

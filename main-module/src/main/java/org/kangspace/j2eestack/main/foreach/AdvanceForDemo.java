package org.kangspace.j2eestack.main.foreach;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Spliterator;
import java.util.function.Consumer;

/**
 * 增强For循环Demo
 * @author kango2gler@gmail.com
 * @since 2022/10/25
 */
public class AdvanceForDemo {

    /**
     * 增强For循环
     */
    public static void advanceFor() {
        List<String> list = new ArrayList<>();
        for (String temp : list) {
            System.out.println(temp);
        }
    }
    /**
     * 自定义类增强For循环
     */
    public static void customClasAdvanceFor() {
        ForObj forObj = new ForObj();
        for (ForObj temp : forObj) {
            System.out.println(temp);
        }
    }

    /**
     * 自定义For循环对象
     */
    public static class ForObj implements Iterable<ForObj>{

        @Override
        public Iterator<ForObj> iterator() {
            return null;
        }

        @Override
        public void forEach(Consumer<? super ForObj> action) {
            Iterable.super.forEach(action);
        }

        @Override
        public Spliterator<ForObj> spliterator() {
            return Iterable.super.spliterator();
        }
    }


    public static void main(String[] args) {

    }


}

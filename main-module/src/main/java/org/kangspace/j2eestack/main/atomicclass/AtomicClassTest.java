package org.kangspace.j2eestack.main.atomicclass;

import java.io.Serializable;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * 2019/12/18 11:20
 *
 * @author kango2gler@gmail.com
 */
public class AtomicClassTest implements Serializable {
    static AtomicInteger i = new AtomicInteger();
    public static void funs(){
        System.out.println("src i:"+i.get());
        System.out.println("++i:"+i.addAndGet(1));
        System.out.println("i++:"+i.getAndAdd(1));
        System.out.println("i:"+i.get());
        System.out.println("++i2:"+i.incrementAndGet());
        System.out.println("--i:"+i.decrementAndGet());
        //只有BoatstrapClassLoader可以调用Unsafe.getUnsafe()方法
//        Unsafe unsafe= Unsafe.getUnsafe();
        Integer inull = null;
        System.out.println(1==inull);
    }

    public static void main(String[] args) {
        funs();
    }
}

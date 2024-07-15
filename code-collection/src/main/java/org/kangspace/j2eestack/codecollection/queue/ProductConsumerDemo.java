package org.kangspace.j2eestack.codecollection.queue;

import java.util.concurrent.CountDownLatch;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.LinkedBlockingQueue;

/**
 * 生产者消费者Demo
 * @author kango2gler@gmail.com
 * @date 2024/6/26
 * @since
 */
public class ProductConsumerDemo {
    public static void main(String[] args) throws InterruptedException {
        // 生产者,消费者
        // 队列
        LinkedBlockingQueue<Integer> queue = new LinkedBlockingQueue<>();
        int cnt = 1;
        // 生产者
        ExecutorService products = Executors.newFixedThreadPool(1);
        for (int i = 0; i < cnt; i++) {
            products.execute(()->{
                while (true) {
                    try {
                        queue.put(Double.valueOf(Math.random() * 100).intValue());
                        Thread.sleep(1000L);
                    } catch (InterruptedException e) {
                        throw new RuntimeException(e);
                    }
                }
            });
        }

        ExecutorService consumers = Executors.newFixedThreadPool(1);
        for (int i = 0; i < cnt; i++) {
            consumers.execute(()->{
                while (true) {
                    try {
                        Integer val = queue.take();
                        System.out.println(val);
                    } catch (InterruptedException e) {
                        throw new RuntimeException(e);
                    }
                }
            });
        }
        new CountDownLatch(1).await();
    }
}


package org.kangspace.j2eestack.main.multithread;

import java.util.concurrent.LinkedBlockingDeque;
import java.util.concurrent.ThreadFactory;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;


/**
 * 多线程ThreadPoolExecutor执行中的异常<br>
 * 1. Future future = executorService.submit(); submit任务后, 若任务中出现异常,不会抛出, 使用future.get();可触发异常<br>
 * 2. void executorService.execute(runnable) 中有异常时候，如果不指定Thread.uncaughtExceptionHandler, 那么只会在控制台打印System.error， 如果没开启控制台输出，就不会有任何感知<br>
 *
 * @author kango2gler@gmail.com
 * @since 2023/7/27
 */
public class ExceptionInExecutor {
    private static final ThreadPoolExecutor executorService =
            new ThreadPoolExecutor(20, 20, 0, TimeUnit.SECONDS,
                    new LinkedBlockingDeque<>(),
                    new ThreadFactory() {
                        private int threadInitNumber = 0;

                        private synchronized int nextThreadNum() {
                            return threadInitNumber++;
                        }

                        private String getName() {
                            return "ExceptionInExecutor-" + nextThreadNum();
                        }

                        @Override
                        public Thread newThread(Runnable r) {
                            return new Thread(r, getName());
                        }
                    });

    /**
     * 多线程中默认异常抛出测试
     */
    public static void exceptionInExecutor() throws InterruptedException {
       Thread thread = new Thread(()-> {
           System.out.println(Thread.currentThread().getName() + ":" + "执行开始");
            for (int i = 0; i < 10; i++) {
                int finalI = i;
                // submit任务后, 若任务中出现异常,不会抛出, 使用future.get();可触发异常
                // Future<?> future = executorService.submit(() -> {});
                // execute任务后, 若任务中出现异常, 不会抛出, 会在控制台打印System.error
                // execute(runnable) 中有异常时候，如果不指定Thread.uncaughtExceptionHandler, 那么只会在控制台打印System.error， 如果没开启控制台输出，就不会有任何感知
                executorService.execute(() -> {
                    System.out.println(Thread.currentThread().getName() + ":" + Thread.getDefaultUncaughtExceptionHandler()+":" + Thread.currentThread().getThreadGroup());
                    if (finalI % 2 == 0) {
                        throw new RuntimeException("%2 exception");
                    }
                    System.out.println(Thread.currentThread().getName() + ": i: " + finalI);
                });
            }
            executorService.shutdown();
            System.out.println(Thread.currentThread().getName() + ":" + "执行结束");
        });
        thread.start();
        thread.join();
    }

    public static void main(String[] args) throws InterruptedException {
        exceptionInExecutor();
    }
}

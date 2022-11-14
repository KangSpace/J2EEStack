package org.kangspace.j2eestack.main.util;

/**
 * @author kango2gler@gmail.com
 * @desc 控制台输出日志对象
 * @date 2017/6/22 15:06
 */
public class ConsoleLogger {
    public void println(String msg){
        System.out.println(msg);
    }

    public void info(String msg){
        println(msg);
    }

}

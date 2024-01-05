package org.kangspace.j2eestack.main.directio;

import lombok.extern.slf4j.Slf4j;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;

/**
 * 直接IO测试
 * @author kango2gler@gmail.com
 * @date 2024/1/3 16:41
 */
@Slf4j
public class DirectIOTest {

    /**
     * ByteBuffer测试(DirectByteBuffer直接内存, 直接申请非堆内存)
     */
    public static void bytebufferTest(){
        //1.创建DirectByteBuffer, 1.5G
//        int byteSize = Double.valueOf(1.5 *1000).intValue()*1024*1024;
        // 1K
        int byteSize = 1024;
        ByteBuffer bytebuffer = ByteBuffer.allocateDirect(byteSize);
        byte[] helloBytes = "hello".getBytes();
        bytebuffer.put(helloBytes);
        byte[] newHelloBytes = new byte[helloBytes.length];
        bytebuffer.get(newHelloBytes);
        log.info("get hello: {}", new String(newHelloBytes));
        bytebuffer.flip();
        bytebuffer.limit(byteSize);
        bytebuffer.get(newHelloBytes);
        log.info("get hello: {}", new String(newHelloBytes));
        int pos = bytebuffer.position();
        bytebuffer.putLong(Long.MAX_VALUE);
        bytebuffer.position(pos);
        log.info("get long: {}", bytebuffer.getLong());
        bytebuffer.flip();
        bytebuffer.limit(byteSize);
        log.info("get hello/long?: {}", bytebuffer.get());
        log.info("申请直接内存: {}", byteSize);
        //2.创建DirectByteBuffer的数组
        //3.将数组中的DirectByteBuffer放入到DirectByteBuffer数组中
        //4.将DirectByteBuffer数组放入到ByteBuffer数组中
        //5.将ByteBuffer数组放入到ByteBuffer数组中
        //6.将ByteBuffer数组中的ByteBuffer放入到ByteBuffer数组中
        //7.将ByteBuffer数组中的ByteBuffer放入到DirectByteBuffer数组中
        //8.将DirectByteBuffer数组中的DirectByteBuffer放入到
    }

    /**
     * FileChannel测试(sendfile, 使用 FileChannel 的 transferTo() 或 transferFrom() 方法来实现 sendfile 的功能)
     */
    public static void fileChannelTest(){
        try (FileInputStream inFile = new FileInputStream("/var/temp/source.txt");
             FileOutputStream outFile = new FileOutputStream("/var/temp/destination.txt")) {

            FileChannel inChannel = inFile.getChannel();
            FileChannel outChannel = outFile.getChannel();
            long transferred = 0;
            long fileSize = inChannel.size();

            while (transferred < fileSize) {
                transferred += inChannel.transferTo(transferred, fileSize - transferred, outChannel);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    public static void main(String[] args) {
        bytebufferTest();
    }
}

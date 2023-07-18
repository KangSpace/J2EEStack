package org.kangspace.j2eestack.codecollection.cache;


import org.springframework.data.redis.core.RedisTemplate;

import java.util.List;
import java.util.Map;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

/**
 * Redis缓存Service
 *
 * @author kango2gler@gmail.com
 * @since 2022/10/28
 */
public interface RedisCachedService<RedisTemplateValueType,KEY_PATTERN> extends CachedService<KEY_PATTERN> {

    /**
     * 获取RedisTemplate
     *
     * @return {@link RedisTemplate}
     */
    RedisTemplate<String, RedisTemplateValueType> redisTemplate();

    @Override
    default  <T> T getCacheValue(String key) {
        return (T) redisTemplate().opsForValue().get(key);
    }

    /**
     * 获取hash值
     * @param key redis key
     * @param hashKeys hash key列表
     * @return 对应hash值
     */
    default  <T> List<T> getCacheHashValue(String key, List hashKeys) {
        return (List<T>) redisTemplate().boundHashOps(key).multiGet(hashKeys);
    }
    /**
     * 获取存在的hash值
     * @param key redis key
     * @param hashKeys hash key列表
     * @return 对应hash值
     */
    default  <T> List<T> getCacheHashExistsValue(String key, List hashKeys) {
        return (List<T>) (getCacheHashValue(key, hashKeys)).stream().filter(t->t!=null).collect(Collectors.toList());
    }

    /**
     * 设置Hash值
     * @param key redis key
     * @param map hash 值
     * @param ttlSeconds 超时时间,秒
     */
    default void setCacheHashValue(String key, Map map, Long ttlSeconds) {
        redisTemplate().boundHashOps(key).putAll(map);
        redisTemplate().boundHashOps(key).expire(ttlSeconds, TimeUnit.SECONDS);
    }

    @Override
    default <T> Boolean setCacheValue(String key, T value, Long ttlSeconds) {
        if(value instanceof List){
            RedisTemplateValueType[] values = (RedisTemplateValueType[]) ((List<RedisTemplateValueType>) value).toArray();
            redisTemplate().boundListOps(key).leftPushAll(values);
        }else {
            redisTemplate().opsForValue().set(key, (RedisTemplateValueType) value, ttlSeconds, TimeUnit.SECONDS);
        }
        return true;
    }

    @Override
    default Boolean clearCache(String key){
        return redisTemplate().delete(key);
    }

    /**
     * 获取锁
     * @param key key
     * @return boolean
     */
    default Boolean tryLock(String key, Long ttlSeconds) {
        return redisTemplate().opsForValue().setIfAbsent(key, null, ttlSeconds, TimeUnit.SECONDS);
    }

    /**
     * 删除锁
     * @param key key
     * @return boolean
     */
    default Boolean releaseLock(String key) {
        return redisTemplate().delete(key);
    }

    /**
     * 减值(key不存在时返回-1)
     * @param key key
     * @return 最新值
     */
    default Long decrement(String key){
        return redisTemplate().opsForValue().decrement(key);
    }
}
